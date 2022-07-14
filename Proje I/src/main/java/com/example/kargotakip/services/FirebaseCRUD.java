package com.example.kargotakip.services;

import com.example.kargotakip.models.Location;
import com.google.api.core.ApiFuture;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.*;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.example.kargotakip.models.User;
import javafx.concurrent.Task;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.ExecutionException;

public class FirebaseCRUD {
    public static void getFirebase() throws IOException {
        ClassLoader classLoader = FirebaseCRUD.class.getClassLoader();
        File file = new File(Objects.requireNonNull(classLoader.getResource("serviceAccountKey.json")).getFile());
        FileInputStream serviceAccount = new FileInputStream(file.getAbsolutePath());
        FirebaseOptions options = new FirebaseOptions.Builder()
                .setCredentials(GoogleCredentials.fromStream(serviceAccount))
                .build();

        FirebaseApp.initializeApp(options);
    }

    public static List<User> getUsers() throws ExecutionException, InterruptedException {
        List<User> users = new ArrayList<>();
        Firestore dbFirestore = FirestoreClient.getFirestore();
        CollectionReference collectionReference = dbFirestore.collection("users");
        ApiFuture<QuerySnapshot> future = collectionReference.get();
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();
        for (DocumentSnapshot document : documents) {
            User crud = new User();
            if (document.exists()) {
                crud.toUser(document);
                users.add(crud);
            }
        }

        return users;
    }

    public static List<Location> getLocations() throws ExecutionException, InterruptedException {
        List<Location> konumlar = new ArrayList<>();
        Firestore dbFirestore = FirestoreClient.getFirestore();
        CollectionReference collectionReference = dbFirestore.collection("locations");
        ApiFuture<QuerySnapshot> future = collectionReference.get();
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();
        for (DocumentSnapshot document : documents) {
            Location konum = new Location();
            if (document.exists()) {
                konum.toLocation(document);
                konumlar.add(konum);
            }
        }

        return konumlar;
    }

    public static List<Location> getDagitimSil(int size) throws ExecutionException, InterruptedException {
        List<QueryDocumentSnapshot> documents;
        List<Location> konumlar;
        do {
            konumlar = new ArrayList<>();
            Firestore dbFirestore = FirestoreClient.getFirestore();
            CollectionReference colRef = dbFirestore.collection("dagitim");
            ApiFuture<QuerySnapshot> future = colRef.get();
            documents = future.get().getDocuments();
        }while (size <= documents.size());

        for (DocumentSnapshot document : documents) {
            if (document.exists()) {
                konumlar.add(getSingleLocation(Objects.requireNonNull(document.get("konumID")).toString()));
            }
        }
        return konumlar;
    }

    public static List<Location> getDagitimEkle(int size) throws ExecutionException, InterruptedException {
        List<QueryDocumentSnapshot> documents;
        List<Location> konumlar;
        do {
            konumlar = new ArrayList<>();
            Firestore dbFirestore = FirestoreClient.getFirestore();
            CollectionReference colRef = dbFirestore.collection("dagitim");
            ApiFuture<QuerySnapshot> future = colRef.get();
            documents = future.get().getDocuments();
        }while (size >= documents.size());

        for (DocumentSnapshot document : documents) {
            if (document.exists()) {
                konumlar.add(getSingleLocation(Objects.requireNonNull(document.get("konumID")).toString()));
            }
        }
        return konumlar;
    }

    public static Location getSingleLocation(String id) throws ExecutionException, InterruptedException {
        Firestore dbFirestore = FirestoreClient.getFirestore();
        DocumentReference documentReference = dbFirestore.collection("locations").document(id);
        ApiFuture<DocumentSnapshot> future = documentReference.get();
        DocumentSnapshot document = future.get();
        Location konum = new Location();
        if (document.exists()) {
            konum.toLocation(document);
        }

        return konum;
    }

    public static void adresEkle(Location konum) {
        Firestore dbFirestore = FirestoreClient.getFirestore();
        dbFirestore.collection("dagitim").document(randomString()).set(konum.toMap());
    }

    public static void deleteDagitim(Location konum) throws ExecutionException, InterruptedException {
        Firestore dbFirestore = FirestoreClient.getFirestore();
        ApiFuture<QuerySnapshot> future = dbFirestore.collection("dagitim").whereEqualTo("konumID", konum.getId()).get();
        List<QueryDocumentSnapshot> list = future.get().getDocuments();
        String id = list.get(0).getId();
        dbFirestore.collection("dagitim").document(id).delete();
    }

    public static void createUser(User user) {
        Firestore dbFirestore = FirestoreClient.getFirestore();
        dbFirestore.collection("users").document(randomString()).set(user.toMap());
    }

    public static String randomString() {
        int leftLimit = 97;
        int rightLimit = 122;
        int targetStringLength = 10;
        Random random = new Random();

        return random.ints(leftLimit, rightLimit + 1)
                .limit(targetStringLength)
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();
    }
}