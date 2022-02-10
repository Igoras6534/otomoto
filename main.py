from commands import setup,add,search,delete,cli

cli.add_command(setup)
cli.add_command(add)
cli.add_command(search)
cli.add_command(delete)




if __name__=="__main__":
    cli()