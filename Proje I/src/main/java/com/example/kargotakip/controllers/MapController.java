package com.example.kargotakip.controllers;

import com.example.kargotakip.models.Location;
import com.example.kargotakip.services.Browser;
import javafx.fxml.FXML;
import javafx.scene.layout.AnchorPane;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class MapController {
    @FXML
    public AnchorPane root;
    private List<Location> path;

    public void setData(List<Location> path) {
        this.path = path;
        Browser browser = new Browser(root, path);
        browser.createMap();
    }
}