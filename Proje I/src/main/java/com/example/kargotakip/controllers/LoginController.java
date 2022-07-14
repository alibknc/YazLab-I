package com.example.kargotakip.controllers;

import com.example.kargotakip.models.User;
import com.example.kargotakip.services.FirebaseCRUD;
import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import lombok.SneakyThrows;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.Objects;
import java.util.ResourceBundle;

@Component
public class LoginController implements Initializable {
    public List<User> users;

    @FXML
    private AnchorPane ekran;

    @FXML
    private TextField girisEmail;

    @FXML
    private PasswordField girisSifre;

    @FXML
    private Button girisBtn;

    @FXML
    private TextField kayitEmail;

    @FXML
    private PasswordField kayitSifre;

    @FXML
    private Button kayitBtn;

    @FXML
    private ProgressIndicator pi;

    @FXML
    private ProgressIndicator pi2;

    @FXML
    private Label lblError;

    @FXML
    private Label lblError2;

    @FXML
    public void girisButon(ActionEvent event) {
        if (event.getSource() == girisBtn) {
            if (login().equals("true")) {
                Task<Scene> task = girisGorev();
                pi.progressProperty().bind(task.progressProperty());
                task.setOnSucceeded(e -> {
                    Scene result = task.getValue();
                    ekran.getChildren().remove(pi);
                    Node node = (Node) event.getSource();
                    Stage stage = (Stage) node.getScene().getWindow();
                    stage.setScene(result);
                });
                Thread thread = new Thread(task);
                thread.start();
            }
        }
    }

    @FXML
    void kayitOl(ActionEvent event) {
        if (event.getSource() == kayitBtn) {
            if (kayit().equals("true")) {
                Task<Scene> task = girisGorev();
                pi2.progressProperty().bind(task.progressProperty());
                task.setOnSucceeded(e -> {
                    Scene result = task.getValue();
                    Node node = (Node) event.getSource();
                    Stage stage = (Stage) node.getScene().getWindow();
                    stage.setScene(result);
                });
                Thread thread = new Thread(task);
                thread.start();
            }
        }
    }

    @SneakyThrows
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        FirebaseCRUD.getFirebase();
        users = FirebaseCRUD.getUsers();
    }

    private Task<Scene> girisGorev() {
        return new Task<>() {
            @Override
            protected Scene call() {
                Scene scene;
                try {
                    scene = new Scene(FXMLLoader.load(Objects.requireNonNull(getClass().getResource("/FXMLs/home.fxml"))));
                    return scene;
                } catch (IOException ex) {
                    System.out.println(ex.getMessage());
                }
                return null;
            }
        };
    }

    private String login() {
        String email = girisEmail.getText();
        String sifre = girisSifre.getText();

        for(User user : users){
            if(user.getEmail().equals(email)){
                if(user.getPassword().equals(sifre)){
                    lblError.setText("Giriş Başarılı");
                    return "true";
                }else{
                    lblError.setText("Hatalı Şifre! Tekrar Deneyin.");
                    return "false";
                }
            }
        }
        lblError.setText("Kullanıcı Bulunamadı");
        return "false";
    }

    private String kayit() {
        String email = kayitEmail.getText();
        String sifre = kayitSifre.getText();

        if(!email.isEmpty() && !sifre.isEmpty()){
            for(User user : users){
                if(user.getEmail().equals(email)){
                    lblError2.setText("Kullanıcı mevcut. Giriş yapınız.");
                    return "false";
                }
            }
            User temp = new User();
            temp.setEmail(email);
            temp.setPassword(sifre);
            FirebaseCRUD.createUser(temp);
            lblError2.setText("Kayıt Başarılı");
            return "true";
        }
        lblError2.setText("Eksik giriş. Tekrar deneyin.");
        return "false";
    }
}