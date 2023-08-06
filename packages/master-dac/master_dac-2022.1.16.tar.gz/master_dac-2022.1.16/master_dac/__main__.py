import importlib
from typing import List
import click
import sys
import logging
logging.basicConfig(level=logging.INFO)
from .configuration import Configuration
from .utils import check_last_masterdac

original_args = [arg for arg in sys.argv]

@click.group()
def main():
    pass


@main.group()
def courses():
    """Permet de gérer la liste des cours suivis"""
    pass

@click.argument("courses", type=click.Choice(["amal", "rld"]), nargs=-1)
@courses.command("add")
def courses_add(courses: List[str]):
    """Ajout de cours"""
    configuration = Configuration()
    configuration.courses.update(courses)
    configuration.save()

@courses.command("list")
def courses_list():
    """Liste des cours"""
    for course in Configuration().courses:
        print(course)

@click.option("--no-self-update", is_flag=True)
@main.command()
def update(no_self_update: bool):
    """Mettre à jour l'ensemble des modules pour les cours suivis"""
    if not no_self_update:
        check_last_masterdac(original_args)

    # Check that package are installed

    configuration = Configuration()
    install = importlib.import_module("master_dac.install")

    processed = set()
    for course in configuration.courses:
        getattr(install, course)(processed)

    print("Don't forget to download the datasets with `master-dac download-datasets`")

@main.command()
def download_datasets():
    """Mettre à jour l'ensemble des jeux de données pour les cours suivis"""
    configuration = Configuration()
    install = importlib.import_module("master_dac.datasets")

    for course in configuration.courses:
        getattr(install, course, lambda *args: None)()
