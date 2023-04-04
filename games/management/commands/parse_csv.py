import csv
import os
import pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DatabaseError

from games.models import Year, Genre, Platform, Publisher, Game

class Command