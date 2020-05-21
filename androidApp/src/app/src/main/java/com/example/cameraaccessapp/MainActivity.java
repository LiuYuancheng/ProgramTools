package com.example.cameraaccessapp;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Build;
import android.os.Bundle;
import android.security.keystore.KeyProperties;
import android.security.keystore.KeyProtection;
//import android.util.Base64;
import java.util.Base64;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.EditText;

import java.io.IOException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.cameraaccessapp.MESSAGE";
    private static final int CAMERA_REQUEST = 1888;
    ImageView imageView;
    Intent cameraIntent;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Load a background for the current screen from a drawable resource
        getWindow().setBackgroundDrawableResource(R.drawable.ic_launcher_background) ;
        // Set the Activity title by getting a string from the Resources object, because
        //  this method requires a CharSequence rather than a resource ID
        getWindow().setTitle(getResources().getText(R.string.app_name));
        imageView = (ImageView) this.findViewById(R.id.imageView1);
        Button photoButton = (Button) this.findViewById(R.id.button1);

        photoButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(cameraIntent, CAMERA_REQUEST);

            }
        });

    }

    /** Called when the user taps the Send button */
    @RequiresApi(api = Build.VERSION_CODES.M)
    public void sendMessage(View view) throws KeyStoreException, CertificateException, NoSuchAlgorithmException, IOException, UnrecoverableKeyException {
        // Do something in response to button
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText2);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);

        // import a AES 256 key
        //byte[] encodedKey = Base64.decode("14ABB0151E9DDD53EEF6F0A0B25661039DC6A40F9FBD977A", Base64.DEFAULT);
        //SecretKey key = new SecretKeySpec(encodedKey, 0, encodedKey.length, "AES");

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        SecureRandom random = new SecureRandom(); // cryptograph. secure random
        keyGen.init(random);
        SecretKey key = keyGen.generateKey();


        KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");
        keyStore.load(null);
        keyStore.setEntry(
                "key1",
                new KeyStore.SecretKeyEntry(key),
                new KeyProtection.Builder(KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT)
                        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                        .build());
        SecretKey keyStoreKey = (SecretKey) keyStore.getKey("key1", null);

        byte encoded[] = keyStoreKey.getEncoded();
        //String stringKey = Base64.getEncoder().encodeToString(encoded);

        String stringKey = keyStoreKey.toString();
        System.out.println("============>" + stringKey);

    }

    public void onActivityResult(View view) {
        System.out.println("123123");


        Bitmap photo = (Bitmap) cameraIntent.getExtras().get("data");
        imageView.setImageBitmap(photo);

    }

}
