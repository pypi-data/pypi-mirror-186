
import quacker
import typer
app = typer.Typer()


@app.command()
def get_conformers_by_energy(mole_name_folder, energy_level):
    return quacker.get_conformers_by_energy(mole_name_folder, energy_level)


@app.command()
def get_conformers(mole_name_folder):
    return quacker.get_conformers(mole_name_folder)


@app.command()
def del_conformers(basename):
    return quacker.del_conformers(basename)


@app.command()
def replace_conformers(folder):
    return quacker.replace_conformers(folder)


@app.command()
def put_conformers(folder):
    return quacker.put_conformers(folder)
