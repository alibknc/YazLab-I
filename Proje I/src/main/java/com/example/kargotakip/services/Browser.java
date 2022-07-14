package com.example.kargotakip.services;

import com.example.kargotakip.models.Location;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Line;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import java.util.List;

public class Browser {
    private final AnchorPane ap;
    private final WebView webView;
    private final WebEngine webEngine;
    private final MapService mapService = new MapService();
    private final List<Location> pathList;

    public Browser(AnchorPane root, List<Location> path) {
        this.pathList = path;
        webView = new WebView();
        this.ap = root;
        webEngine = webView.getEngine();
    }

    public void createMap() {
        ap.getChildren().removeAll(ap.getChildren());
        webEngine.load(mapService.createMap(pathList));
        ap.getChildren().add(webView);
        yoluCiz(pathList);
    }

    public void yoluCiz(List<Location> konumlar) {
        Line line = new Line();
        int startX = 399;
        line.setStartX(startX);
        int startY = 270;
        line.setStartY(startY);
        for (Location konum : konumlar) {
            line.setEndX(konum.getLineX());
            line.setEndY(konum.getLineY());
            ap.getChildren().add(line);
            line = new Line();
            line.setStartX(konum.getLineX());
            line.setStartY(konum.getLineY());
        }
    }
}