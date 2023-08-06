#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:37:19 2022

@author: akshay
"""
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output,State

def getAlgoHeader(algo):
    return dbc.Row([
     dbc.Col(dbc.Checklist(options=[{"label": algo,"value": True}],
                                    value=[],
                                    id=algo,
                                    inline=True,switch=True,labelStyle={"font-weight": "bold",
                                                                        "font-size": "18px"},
                                    labelCheckedStyle={"color": "green"},persistence=True,persistence_type="memory"),
              width={"size": 9},),
   dbc.Col(dbc.Button("Parameters",id=algo+"-collapse-button",
            className="mr-1",size="sm",color="light",n_clicks=0,style={"margin-top": "15px"}),
        width={"size": 3},)
       ])


    #--------------------------    
def genrateCollapseCallback(id):
    @app.callback(
        Output(id+"-collapse", "is_open"),
        [Input(id+"-collapse-button", "n_clicks")],
        [State(id+"-collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open