package com.example.kargotakip.controllers;

import com.example.kargotakip.models.Location;
import com.example.kargotakip.services.FirebaseCRUD;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import org.springframework.stereotype.Component;

import java.util.concurrent.ExecutionException;

@Component
public class ListItemController {
    @FXML
    Label konumAdi;

    @FXML
    Label id;

    @FXML
    Button silBtn;
    private Location konum;
    private HomeController hc;

    public void adresSil() throws ExecutionException, InterruptedException {
        FirebaseCRUD.deleteDagitim(konum);
        hc.listeGuncelleSil();
    }

    public void setData(Location konum, int sira, HomeController hc) {
        this.hc = hc;
        this.konum = konum;
        konumAdi.setText(konum.getKonumAdi());
        id.setText(Integer.toString(sira));
        silBtn.setOnAction(e -> {
            try {
                adresSil();
            } catch (ExecutionException | InterruptedException ex) {
                ex.printStackTrace();
            }
        });
    }
}