#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import json

import boto3
import math
import re
import os
from botocore.exceptions import ClientError

MANDATORY_REGION = 'eu-west-3'
AWS_ARN_PATTERN = R"^arn:(?P<Partition>[^:\n]*):" \
                  R"(?P<Service>[^:\n]*):" \
                  R"(?P<Region>[^:\n]*):" \
                  R"(?P<AccountID>[^:\n]*):" \
                  R"(?P<Ignore>(?P<ResourceType>[^:\/\n]*)[:\/])?(?P<Resource>.*)$"


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class S3Glacier:
    def __init__(self, bucket_name: str):
        self._bucket_name = bucket_name
        self._session = boto3.session.Session()
        self._s3 = self._session.resource('s3')

        try:
            self._s3.meta.client.head_bucket(Bucket=bucket_name)
            # bucket = self._s3.Bucket(S3_BUCKET_NAME)
        except ClientError as err:
            raise RuntimeError(f"Bucket {bucket_name} not found")

        self._bucket = self._s3.Bucket(bucket_name)

    @property
    def name(self):
        return self._bucket_name

    @property
    def bucket(self):
        return self._bucket

    @property
    def account_id(self):
        sts = boto3.client('sts')
        return sts.get_caller_identity()['Account']

    def get_projects(self):
        projects = dict()

        pattern = r'projects/(?P<project_code>.+)/(?P<filename>(?:.+).tar.gz)'
        for obj in self._bucket.objects.all():
            groups = re.match(pattern, obj.key)
            try:
                project_code = groups['project_code']
            except:
                continue

            if project_code not in projects:
                projects[project_code] = {
                    'nb_files': 0,
                    'total_size_in_bytes': 0,
                    'files': []
                }

            projects[project_code]['nb_files'] += 1
            projects[project_code]['total_size_in_bytes'] += obj.size
            projects[project_code]['files'].append(
                {
                    'name': os.path.basename(obj.key),
                    'key': obj.key,
                    'last_modified': str(obj.last_modified),
                    'size_in_bytes': obj.size,
                    'storage_class': obj.meta.data['StorageClass']
                }
            )

        # print(projects)

        return projects

    def is_project(self, project_code: str):
        pass

    def _get_normalized_sns_topic_name(self):
        return f"{self._bucket_name}-sns-topic"

    def get_bucket_topic(self):
        sns = self._session.resource('sns')
        topic_name = self._get_normalized_sns_topic_name()

        bucket_topic = None
        for topic in sns.topics.all():
            if re.match(AWS_ARN_PATTERN, topic.arn)["Resource"] == topic_name:
                bucket_topic = topic
                break

        if bucket_topic is None:
            # No topic associated with this vault, creating it with proper name
            # if self._verbose:
            print(f"No topic with name {topic_name} were found. We just created it...")

            bucket_topic = sns.create_topic(Name=topic_name)

            # https://stackoverflow.com/questions/49961491/using-boto3-to-send-s3-put-requests-to-sns

            # Set topic policy to accept s3 events
            # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_topic_attributes
            sns_topic_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": "sns:Publish",
                        "Resource": bucket_topic.arn,
                        "Condition": {
                            "ArnLike": {"AWS:SourceArn": f"arn:aws:s3:*:*:{self._bucket_name}"},
                        },
                    },
                ],
            }

            bucket_topic.set_attributes(
                AttributeName='Policy',
                AttributeValue=json.dumps(sns_topic_policy)
            )

            # Set notification config
            notification = self._bucket.Notification()

            notification.put(NotificationConfiguration={
                'TopicConfigurations': [
                    {
                        'TopicArn': bucket_topic.arn,
                        'Events': [  # s3 Events we want to trig notification
                            's3:ObjectCreated:*',
                            's3:ObjectRemoved:*',
                            's3:ObjectRestore:*'
                        ]
                    }
                ]
            }
            )

        return bucket_topic

    def subscribe_to_bucket_notifications(self, email: str):
        # 1- on veut recuperer le topic associe a ce bucket
        bucket_topic = self.get_bucket_topic()

        # Getting subscriptions
        for subscription in bucket_topic.subscriptions.all():
            if subscription.arn == 'PendingConfirmation':
                continue

            if subscription.attributes['Endpoint'] == email:
                # if self._verbose:
                #     print(f"\t-> Email address {email} is already subscribing to this vault topic")
                return None

        subscription = bucket_topic.subscribe(Protocol='email', Endpoint=email)

        return subscription

    def list_subscriptions(self):
        vault_topic = self.get_bucket_topic()

        subscriptions = list()
        for subscription in vault_topic.subscriptions.all():
            if subscription.arn == 'PendingConfirmation':
                subscriptions.append('Pending Subscription')

            else:
                subscriptions.append(subscription.attributes['Endpoint'])

        return subscriptions

    def remove_subscription(self, email: str):
        vault_topic = self.get_bucket_topic()

        subscription_to_delete = None
        for subscription in vault_topic.subscriptions.all():
            if subscription.arn == 'PendingConfirmation':
                continue

            if subscription.attributes['Endpoint'] == email:
                subscription_to_delete = subscription

        if subscription_to_delete is not None:
            subscription_to_delete.delete()
            print(f'This subscription is deleted')
        else:
            # TODO: comme tout ailleurs, ne pas avoir de print interne mais plutot retourner ce qui va bien
            #  cmme code pout faire du print externe !!
            print(f'\t> Email address {email} was not subscribing to the vault notifications')

    # def upload_file(self, file: str, project: str, client: str, description: str):
    def upload_file(self, file: str, project: str):

        # TODO: tester si project est valide (RDX, SCE etc...)

        key = f"projects/{project}/{os.path.basename(file)}"

        # TODO: tester si on a pas deja la cle...
        # Dans l'idee, si le projet existe deja, on va recuperer les infos client et description pour les reinjecter
        # dans les nouveaux fichiers...

        # C'est ici qu'on dit qu'on fait du deep archive !!!
        ExtraArgs = {
            'Metadata': {
                'project': project,
                # 'client': client,
                # 'description': description
            },
            'StorageClass': 'DEEP_ARCHIVE'
        }

        self._bucket.upload_file(file, key, ExtraArgs=ExtraArgs)

    def download_file(self, key: str, output_dir: str):

        file = os.path.basename(key)

        # Where to download ?
        target = os.path.join(output_dir, file)
        print(target)

        try:
            self._bucket.download_file(key, target)  # plante si deep archive...
            return

        except ClientError:
            # File was not available to download, sending restore request
            s3_object = self._bucket.Object(key)
            s3_object.restore_object(
                RestoreRequest={
                    'Days': 5
                }
            )

            print("\t> Object is not accessible yet. Restoring it. The file will be available in a few hours.")
