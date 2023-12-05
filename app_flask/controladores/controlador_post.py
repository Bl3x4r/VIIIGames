from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_usuario import Usuario
from app_flask import app
from flask_bcrypt import Bcrypt