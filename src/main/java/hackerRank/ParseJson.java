package hackerRank;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;

/**
 * Created by sergei on 24.7.17.
 */
public class ParseJson {
    public static void main(String[] args) {
        HttpURLConnection conn = null;

        try {
            URL url = new URL("http://www.nbrb.by/API/ExRates/Currencies");
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Accept", "application/json");

            if (conn.getResponseCode() != 200) {
                throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));

            String output;
            StringBuffer sb = new StringBuffer();
            while ((output = br.readLine()) != null) {
                sb.append(output);
            }
            output = sb.toString();
            System.out.println(output);


            JSONParser parser = new JSONParser();
            Object obj = parser.parse(output);
            JSONArray array = (JSONArray) obj;
            Iterator<JSONObject> iterator = array.iterator();
            while (iterator.hasNext()) {
                System.out.println(iterator.next().get("Cur_Name"));
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (conn != null) {
                conn.disconnect();
            }
        }
    }
}
