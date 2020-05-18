package com.example.cameraaccessapp;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.EditText;

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
    public void sendMessage(View view) {
        // Do something in response to button
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText editText = (EditText) findViewById(R.id.editText2);
        String message = editText.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    public void onActivityResult(View view) {
        System.out.println("123123");


        Bitmap photo = (Bitmap) cameraIntent.getExtras().get("data");
        imageView.setImageBitmap(photo);

    }

}
