#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import argparse
import os
from igloo.S3Glacier import S3Glacier, convert_size
from igloo import __version__
from botocore.exceptions import ClientError

DEFAULT_S3_BUCKET = 'dice-projects-archive'


def list(args):
    s3_glacier = S3Glacier(args.bucket_name)

    projects = s3_glacier.get_projects()

    if args.project:
        # Is the project existing?
        if args.project not in projects:
            raise RuntimeError(f"Project {args.project} not found")

        print(args.project)
        print("\t  {:<40}{:<15}{:<30}{:<20}{:<100}\n".format('FILE', 'SIZE', 'LAST MODIFIED', 'STORAGE CLASS', 'KEY'))
        for file in projects[args.project]['files']:
            print("\t* {:<40}{:<15}{:<30}{:<20}{:<100}".format(
                file['name'],
                convert_size(file['size_in_bytes']),
                file['last_modified'],
                file['storage_class'],
                file['key']
            ))

        return

    # List every projects
    total_size = 0
    for project_code in projects:
        print(project_code)
        print(f"\tNb files: {projects[project_code]['nb_files']}")
        print(f"\tSize:     {convert_size(projects[project_code]['total_size_in_bytes'])}")
        total_size += projects[project_code]['total_size_in_bytes']

    print(f"\n> TOTAL BUCKET SIZE: {convert_size(total_size)}")


def subscribe(args):
    s3_glacier = S3Glacier(args.bucket_name)

    if args.list:
        print("\nList of subscriptions:")
        for subscription_email in s3_glacier.list_subscriptions():
            print(f"\t* {subscription_email}")

    if args.email:
        print(f"\nSubscribing to notifications with email address {args.email}")
        if s3_glacier.subscribe_to_bucket_notifications(args.email) is not None:
            input(
                f"\n\tConfirmation email sent to {args.email}."
                # f"\n\tIt MUST have the following topic arn name in the message body: \"{arn}\""
                f"\n\tPlease check your messages and follow the instructions."
                f"(\n\tDon't forget to check your junk box"
                f"\n\n\tPLEASE PROCEED RIGHT NOW! :-)"
                f"\n\n\tPress Enter to continue..."
            )
        else:
            print(f"{args.email} was already subscribing")

    if args.remove:
        print(f"\nRemoving email address {args.remove} from the subscriptions")
        s3_glacier.remove_subscription(args.remove)


def publish(args):
    s3_glacier = S3Glacier(args.bucket_name)
    vault_topic = s3_glacier.get_bucket_topic()
    vault_topic.publish(
        Subject=f"[{s3_glacier.name}] {args.subject}",
        Message=args.message
    )


def upload(args):
    s3_glacier = S3Glacier(args.bucket_name)
    s3_glacier.upload_file(args.file, args.project)


def download(args):
    s3_glacier = S3Glacier(args.bucket_name)
    projects = s3_glacier.get_projects()
    if args.project not in projects:
        raise RuntimeError(f"{args.project} not found")

    # TODO: ajouter un output-dir dans la cli...
    output_dir = os.getcwd()

    project = projects[args.project]
    for file in project['files']:
        try:
            s3_glacier.download_file(file['key'], output_dir)
        except ClientError as err:
            print("\t> File restore already in progress")


def main():
    parser = argparse.ArgumentParser(
        prog="igloo",
        description="A command line tool to manage archive of projects data on Amazon S3 Glacier Deep Archive",
        epilog="Copyright: D-ICE ENGINEERING"
    )

    parser.add_argument("-v", "--version", action='store_true', help="Show version and exit")

    subparsers = parser.add_subparsers(title='sub-commands', help='available sub-commands')

    # Sub-parser for the info command
    info_parser = subparsers.add_parser("list", help="Command to get list of projects archives")
    info_parser.add_argument("--bucket-name", type=str, default=DEFAULT_S3_BUCKET,
                             help=f"Bucket name. Default is {DEFAULT_S3_BUCKET}")
    info_parser.add_argument("--project", type=str, help="Ask a list for this specific project code")
    # TODO: ajouter une option --jobs pour avoir des infos sur les jobs (in progress, completed...)
    info_parser.set_defaults(func=list)

    # Sub-parser for the subscribe command
    subscribe_parser = subparsers.add_parser("subscribe", help="Command to subscribe an email address to the vault")
    subscribe_parser.add_argument("--bucket-name", type=str, default=DEFAULT_S3_BUCKET,
                                  help=f"Bucket name. Default is {DEFAULT_S3_BUCKET}")
    subscribe_parser.add_argument("--email", type=str,
                                  help="The email address to use to subscribe to this vault notification service")
    subscribe_parser.add_argument("--remove", type=str,
                                  help="Remove the subscription of this email address")
    subscribe_parser.add_argument("--list", action='store_true', help="List every active subscription emails")
    subscribe_parser.set_defaults(func=subscribe)

    # Sub-parser for the publish command
    publish_parser = subparsers.add_parser("publish", help="Command to publish email to this vault subscribers")
    publish_parser.add_argument("--bucket-name", type=str, default=DEFAULT_S3_BUCKET,
                                help=f"Bucket name. Default is {DEFAULT_S3_BUCKET}")
    publish_parser.add_argument("message", type=str, help="Message to publish")
    publish_parser.add_argument("--subject", type=str, default=f"News",
                                help="Message subject. Default [{vault_name}] News")
    publish_parser.set_defaults(func=publish)

    # Sub-parser for the upload command
    upload_parser = subparsers.add_parser("upload", help="Command to upload archives to S3 glacier")
    upload_parser.add_argument("--bucket-name", type=str, default=DEFAULT_S3_BUCKET,
                               help=f"Bucket name. Default is {DEFAULT_S3_BUCKET}")
    upload_parser.add_argument("file", type=str, help="Archive file to upload to S3 glacier")
    upload_parser.add_argument("--project", type=str, required=True, help="Project code (SCE*, RDX*, etc)")
    upload_parser.add_argument("--client", type=str, required=True, help="The project's client")
    upload_parser.add_argument("--description", type=str, required=True, help="The project's one sentence description")
    upload_parser.set_defaults(func=upload)

    # Sub-parser for the download command
    download_parser = subparsers.add_parser("download", help="Command to download archives from S3 glacier")
    download_parser.add_argument("--bucket-name", type=str, default=DEFAULT_S3_BUCKET,
                                 help=f"Bucket name. Default is {DEFAULT_S3_BUCKET}")
    download_parser.add_argument("--project", type=str, required=True, help="Project code (SCE*, RDX*, etc)")
    download_parser.add_argument("--file", type=str, help="A specific file to download from the project")
    download_parser.set_defaults(func=download)

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(1)

    func = None
    try:
        func = args.func
    except AttributeError:
        # Necessary when igloo is called without any arguments to avoid AttributeError
        parser.error("too few arguments")
    func(args)


if __name__ == '__main__':
    main()
