package com.example.kargotakip.controllers;

import com.example.kargotakip.models.Location;
import com.example.kargotakip.services.FirebaseCRUD;
import com.example.kargotakip.services.ShortestPath;
import javafx.concurrent.Task;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import lombok.SneakyThrows;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.ResourceBundle;

@Component
public class HomeController implements Initializable {
    @FXML
    ChoiceBox<String> konumSec;
    @FXML
    Button konumEkleBtn;
    @FXML
    Button listeGetirBtn;
    @FXML
    Button haritaBtn;
    @FXML
    VBox list;
    @FXML
    HBox hbox;
    public static List<Location> konumlar;
    public List<Location> path;
    public int listeID = 1;
    private MapController mc;

    @SneakyThrows
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        konumlar = FirebaseCRUD.getLocations();
        for (Location konum : konumlar) {
            konumSec.getItems().add(konum.getKonumAdi());
        }
        konumEkleBtn.setVisible(false);
        haritaBtn.setVisible(false);
    }

    @FXML
    public void listeGuncelleEkle() {
        listeGetirBtn.setVisible(false);
        list.getChildren().removeAll(list.getChildren());
        listeID = 1;
        ProgressBar pb = new ProgressBar();
        pb.setProgress(-1F);
        list.getChildren().add(pb);
        Task<List<Location>> task = listeOlusturEkle();
        task.setOnSucceeded(e -> {
            list.getChildren().remove(pb);
            path = task.getValue();
            for (Location konum : path) {
                try {
                    listeEkle(konum);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
            konumEkleBtn.setVisible(true);
            haritaBtn.setVisible(true);
            listeGetirBtn.setVisible(false);
            if(mc != null) mc.setData(path);
        });
        pb.progressProperty().bind(task.progressProperty());
        Thread thread = new Thread(task);
        thread.start();
    }

    public void listeGuncelleSil() {
        list.getChildren().removeAll(list.getChildren());
        listeID = 1;
        ProgressBar pb = new ProgressBar();
        pb.setProgress(-1F);
        list.getChildren().add(pb);
        Task<List<Location>> task = listeOlusturSil();
        task.setOnSucceeded(e -> {
            list.getChildren().remove(pb);
            path = task.getValue();
            for (Location konum : path) {
                try {
                    listeEkle(konum);
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
            konumEkleBtn.setVisible(true);
            haritaBtn.setVisible(true);
            listeGetirBtn.setVisible(false);
            if(mc != null) mc.setData(path);
        });
        pb.progressProperty().bind(task.progressProperty());
        Thread thread = new Thread(task);
        thread.start();
    }

    public Task<List<Location>> listeOlusturEkle() {
        return new Task<>() {
            @Override
            protected List<Location> call() throws Exception {
                List<Location> dagitimlar;
                if(path != null)
                    dagitimlar = FirebaseCRUD.getDagitimEkle(path.size());
                else{
                    dagitimlar = FirebaseCRUD.getDagitimEkle(0);
                }
                ShortestPath shortestPath = new ShortestPath();
                List<Integer> path = shortestPath.tabloOlustur(dagitimlar);
                List<Location> yol = new ArrayList<>();
                for (Integer i : path) {
                    if (i != 0) yol.add(dagitimlar.get(i - 1));
                }
                return yol;
            }
        };
    }

    public Task<List<Location>> listeOlusturSil() {
        return new Task<>() {
            @Override
            protected List<Location> call() throws Exception {
                List<Location> dagitimlar;
                dagitimlar = FirebaseCRUD.getDagitimSil(path.size());
                ShortestPath shortestPath = new ShortestPath();
                List<Integer> path = shortestPath.tabloOlustur(dagitimlar);
                List<Location> yol = new ArrayList<>();
                for (Integer i : path) {
                    if (i != 0) yol.add(dagitimlar.get(i - 1));
                }
                return yol;
            }
        };
    }

    @FXML
    public void konumEkle() {
        if (konumSec.getValue() != null) {
            for (Location konum : konumlar) {
                if (konum.getKonumAdi().equals(konumSec.getValue())) {
                    boolean mevcutMu = false;
                    for(Location x : path){
                        if (Objects.equals(x.getKonumAdi(), konum.getKonumAdi())) {
                            mevcutMu = true;
                            break;
                        }
                    }
                    if(!mevcutMu){
                        konumEkleBtn.setVisible(false);
                        haritaBtn.setVisible(false);
                        FirebaseCRUD.adresEkle(konum);
                        listeGuncelleEkle();
                    }
                }
            }
        }
    }

    @FXML
    public void haritaAc() throws IOException {
        Stage stage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("/FXMLs/map.fxml"));
        Parent root = fxmlLoader.load();
        mc = fxmlLoader.getController();
        mc.setData(path);
        Scene scene = new Scene(root, 800, 600);
        stage.setScene(scene);
        stage.setTitle("Harita");
        stage.show();
    }

    public void listeEkle(Location konum) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("/FXMLs/listItem.fxml"));
        AnchorPane tp = (AnchorPane) fxmlLoader.load();
        ListItemController listeController = fxmlLoader.getController();
        listeController.setData(konum, listeID, this);
        list.getChildren().add(tp);
        listeID++;
    }
}