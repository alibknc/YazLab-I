package com.example.kargotakip.models;

import com.google.cloud.firestore.DocumentSnapshot;

import java.util.HashMap;
import java.util.Map;

public class Location {
    String id;
    String konumAdi;
    String koordinat;
    int lineX;
    int lineY;

    public void toLocation(DocumentSnapshot data){
        this.konumAdi = data.get("konumAdi", String.class);
        this.koordinat = data.get("koordinat", String.class);
        this.id = data.get("id", String.class);
        String line = data.get("line", String.class);
        if(line != null){
            String[] xy = line.split("/");
            this.lineX = Integer.parseInt(xy[0]);
            this.lineY = Integer.parseInt(xy[1]);
        }
    }

    public Map<String, Object> toMap(){
        Map<String, Object> docData = new HashMap<>();
        docData.put("konumID", this.id);
        return docData;
    }

    public String getId() {
        return id;
    }

    public int getLineX() {
        return lineX;
    }

    public int getLineY() {
        return lineY;
    }

    public String getKonumAdi() {
        return konumAdi;
    }

    public String getKoordinat() {
        return koordinat;
    }
}