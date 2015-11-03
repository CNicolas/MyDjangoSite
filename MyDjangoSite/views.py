#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cnicolas
# @Date:   2015-11-03 10:08:37
# @Last Modified by:   cnicolas
# @Last Modified time: 2015-11-03 10:17:59

import requests

from django.http import HttpResponse

def big_index(request):
	res = """<!DOCTYPE html>
		<html lang='fr'>
			<head>
				<meta charset='utf-8'>
				<title>MyDjangoSite</title>
				<link rel='stylesheet' href='../static/css/bootstrap.min.css'>
			</head>
			<body>
				<header id='header' class='page-header'>
					<h1>Salut ! <small>C'est l'index de mon localhost !</small></h1>
				</header>
				<div class='col-sm-4 col-sm-offset-4'>
					<div class='panel panel-info'>
						<div class='panel-heading'>
							<h4 class='panel-title'>
								Projets
							</h4>
						</div>
						<div class='panel-body'>
							<a href='forum/' class='btn-danger btn btn-block' role='button'>Forum</a>
							<a href='#' class='btn-info btn btn-block' role='button'>Rien</a>
						</div>
					</div>
				</div>
			</body>
		</html>"""
	return HttpResponse(content=res)
