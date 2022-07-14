package com.example.kargotakip.models;

import com.google.cloud.firestore.DocumentSnapshot;

import java.util.HashMap;
import java.util.Map;

public class User {
    String email;
    String password;

    public Map<String, Object> toMap(){
        Map<String, Object> docData = new HashMap<>();
        docData.put("email", this.email);
        docData.put("password", this.password);
        return docData;
    }

    public void toUser(DocumentSnapshot data){
        this.email = data.get("email", String.class);
        this.password = data.get("password", String.class);
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }
}