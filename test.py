#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:33:45 2023
Testen der Zwischensvchritte, wird am Schluss gelöscht

@author: amelieschepping
"""

import numpy as np


def find_consecutive_ones(array, k):
    rows, cols = array.shape

    # Überprüfung der horizontalen Sequenzen
    for i in range(rows):
        count = 0  # Zähler für aufeinanderfolgende Einsen
        for j in range(cols):
            if array[i, j] == 1:
                count += 1
                if count == k:
                    print(f"{k} mal hintereinander eine 1 gefunden in Zeile {i}")
                    count = 0  # Zurücksetzen des Zählers
            else:
                count = 0  # Zurücksetzen des Zählers, wenn eine Unterbrechung auftritt

    # Überprüfung der Diagonalen
    for i in range(rows - k + 1):
        for j in range(cols - k + 1):
            count = 0  # Zähler für aufeinanderfolgende Einsen
            for d in range(k):
                if array[i + d, j + d] == 1:
                    count += 1
                    if count == k:
                        print(f"{k} mal hintereinander eine 1 gefunden in Diagonale von Zeile {i} und Spalte {j}")
                        count = 0  # Zurücksetzen des Zählers
                else:
                    count = 0  # Zurücksetzen des Zählers, wenn eine Unterbrechung auftritt


# Beispiel 2D-Array
array = np.array([[1, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]])

# Überprüfung auf 4-mal hintereinander eine 1
find_consecutive_ones(array, 4)

