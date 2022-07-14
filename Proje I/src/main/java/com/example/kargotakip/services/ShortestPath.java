package com.example.kargotakip.services;

import com.example.kargotakip.models.Location;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.util.Collections.swap;

public class ShortestPath {
    public List<Integer> mesafeler = new ArrayList<>();
    public ArrayList<List<Integer>> enKisaSira = new ArrayList<>();
    int[][] mesafeTablo;

    public List<Integer> tabloOlustur(List<Location> konumlar) throws IOException {
        MapService mapService = new MapService();
        int size = konumlar.size() + 1;
        mesafeTablo = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i == 0 && j == 0) {
                    mesafeTablo[i][j] = 0;
                    System.out.print(mesafeTablo[i][j] + " ");
                } else if (i == 0 && j != 0) {
                    mesafeTablo[i][j] = mapService.getDistance("origins=40.7639147%2C29.9333831", "&destinations=" + konumlar.get(j - 1).getKoordinat().split(",")[0] + "%2C" + konumlar.get(j - 1).getKoordinat().split(",")[1]);
                    System.out.print(mesafeTablo[i][j] + " ");
                } else if (i != 0 && j == 0) {
                    mesafeTablo[i][j] = mapService.getDistance("origins=" + konumlar.get(i - 1).getKoordinat().split(",")[0] + "%2C" + konumlar.get(i - 1).getKoordinat().split(",")[1], "&destinations=40.7639147%2C29.9333831");
                    System.out.print(mesafeTablo[i][j] + " ");
                } else {
                    mesafeTablo[i][j] = mapService.getDistance("origins=" + konumlar.get(i - 1).getKoordinat().split(",")[0] + "%2C" + konumlar.get(i - 1).getKoordinat().split(",")[1], "&destinations=" + konumlar.get(j - 1).getKoordinat().split(",")[0] + "%2C" + konumlar.get(j - 1).getKoordinat().split(",")[1]);
                    System.out.print(mesafeTablo[i][j] + " ");
                }
            }
            System.out.println("");
        }
        Integer[] sira = new Integer[size];
        for (int i = 0; i < size; i++) sira[i] = i;
        permute(Arrays.asList(sira), 0);
        mesafeHesapla();

        int enKisa = 0;
        for (int i = 1; i < mesafeler.size(); i++) {
            if (mesafeler.get(i) < mesafeler.get(enKisa)) {
                enKisa = i;
            }
        }

        return enKisaSira.get(enKisa);
    }

    public void mesafeHesapla() {
        for (List<Integer> sira : enKisaSira) {
            int top = 0;
            for (int i = 0; i < sira.size() - 1; i++) {
                top = top + mesafeTablo[sira.get(i)][sira.get(i + 1)];
            }
            mesafeler.add(top);
        }
    }

    public void permute(List<Integer> arr, int k) {
        for (int i = k; i < arr.size(); i++) {
            swap(arr, i, k);
            permute(arr, k + 1);
            swap(arr, k, i);
        }
        if (k == arr.size() - 1) {
            if (arr.get(0) == 0) {
                List<Integer> temp = new ArrayList<>(arr);
                enKisaSira.add(temp);
            }
        }
    }
}