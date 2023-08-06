#!/usr/bin/env python
import click
from scinode.cli.commands import daemon, profile, node, nodetree, web, broker


@click.group(help="CLI tool to manage SciNode")
def cli():
    pass


cli.add_command(daemon.daemon)
cli.add_command(node.node)
cli.add_command(nodetree.nodetree)
cli.add_command(profile.profile)
cli.add_command(web.web)
cli.add_command(broker.broker)


if __name__ == "__main__":
    cli()
