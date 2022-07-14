package com.example.kargotakip.services;

import com.example.kargotakip.models.Location;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.JSONObject;

import java.io.IOException;
import java.util.List;

public class MapService {
    private final String mapLink = "https://maps.googleapis.com/maps/api/staticmap?";
    private final String city = "center=İzmit,Kocaeli&zoom=9&size=800x600&maptype=roadmap";
    private final String center = "&markers=color:red%7Clabel:M%7C40.7639147,29.9333831";
    private final String locations = "&markers=color:blue%7C";
    private final String key = "&key=AIzaSyAIeiZkFCL7I5jMLmoU0UN9xXtgYjQok3M";

    private final String distanceLink = "https://maps.googleapis.com/maps/api/distancematrix/json?";
    private final String start = "origins=40.7639147%2C29.9333831";
    //private final String destination = "&destinations=40.6852912%2C29.5744034";

    public String createMap(List<Location> konumlar) {
        if (konumlar == null)
            return mapLink + city + center + key;
        else {
            StringBuilder noktalar = new StringBuilder();
            for (Location temp : konumlar) {
                noktalar.append(locations);
                noktalar.append(temp.getKoordinat());
            }
            return mapLink + city + center + noktalar + key;
        }
    }

    public int getDistance(String start, String destination) throws IOException {
        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        Request request = new Request.Builder()
                .url(distanceLink + start + destination + "&mode=driving" +
                        "" + key)
                .method("GET", null)
                .build();
        Response response = client.newCall(request).execute();
        JSONObject jsonObject = new JSONObject(response.body().string());
        return jsonObject.getJSONArray("rows").getJSONObject(0).getJSONArray("elements").getJSONObject(0).getJSONObject("distance").getInt("value");
    }
}