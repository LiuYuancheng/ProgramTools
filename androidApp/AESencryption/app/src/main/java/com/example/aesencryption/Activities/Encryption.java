package com.example.aesencryption.Activities;

import android.app.Activity;
import android.os.Bundle;
import android.security.keystore.KeyProperties;
import android.security.keystore.KeyProtection;
import android.text.TextUtils;
import android.util.Base64;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.example.aesencryption.Functions.Encrypt;
import com.example.aesencryption.R;

import java.security.KeyStore;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class Encryption extends Activity {

    @BindView(R.id.etOrjText)
    EditText etOrjText;
    @BindView(R.id.secretkey)
    TextView tvSecretKey;
    @BindView(R.id.sonuc)
    TextView tvSonuc;
    @BindView(R.id.anahtar)
    TextView tvAnahtar;
    @BindView(R.id.encBtn)
    Button encBtn;

    KeyGenerator keyGenerator;
    SecretKey secretKey;
    byte[] secretKeyen;
    String strSecretKey;
    byte[] IV = new byte[16];
    byte[] cipherText;
    SecureRandom random;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.encryption);
        ButterKnife.bind(this);

    }

    @OnClick(R.id.encBtn)
    public void btnEncodeClick() {
        if (TextUtils.isEmpty(etOrjText.getText())) {
            Toast t = Toast.makeText(this, "Fill empty field.", Toast.LENGTH_SHORT);
            t.show();
        } else {
            try {
                /*Keygenerator simetrik şifreleme anahtarı üretmek için kullanılan bir kütüphanedir.Öncelikle KeyGenerator kurulumu yapılır
                 * getInstance ile algoritma isminin bir parametre olarak alınması engellenir.*/
                keyGenerator = KeyGenerator.getInstance("AES");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }

            keyGenerator.init(256);// init yöntemiyle oluşturulan KeyGenerator örneği başlatılır.Burada 256bit değer kullanıldı.
            secretKey = keyGenerator.generateKey();//Kurulum tamamlandıktan sonra generateKey() ile anahtar üretilir.
            secretKeyen=secretKey.getEncoded();
            strSecretKey = encoderfun(secretKeyen);
            tvSecretKey.setText(strSecretKey);

            /*IV, Başlatma Vektörü anlamına gelir, şifreleme sırasında SecretKey ile birlikte kullanılacak isteğe bağlı bir sayıdır. IV, şifreleme işleminin başlangıcına rastgelelik ekler.
             * */
            random = new SecureRandom();
            random.nextBytes(IV);
            SecretKey keyStoreKey = null;
            try {


                KeyStore keyStore = KeyStore.getInstance("AndroidKeyStore");
                keyStore.load(null);
                keyStore.setEntry(
                        "key1",
                        new KeyStore.SecretKeyEntry(secretKey),
                        new KeyProtection.Builder(KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT)
                                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                                .build());
                // Key imported, obtain a reference to it.
                keyStoreKey = (SecretKey) keyStore.getKey("key1", null);

            } catch (Exception e){
                System.out.println("==");
                e.printStackTrace();
            }

            try {
                System.out.println("==========>"+keyStoreKey.toString());
                System.out.println("==========>"+secretKey.toString());
                cipherText = Encrypt.encrypt(etOrjText.getText().toString().trim().getBytes(), secretKey, IV);
                //cipherText = Encrypt.encrypt(etOrjText.getText().toString().trim().getBytes(), keyStoreKey, IV);

                Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
                IvParameterSpec ivSpec = new IvParameterSpec(IV);
                cipher.init(Cipher.ENCRYPT_MODE, keyStoreKey);
                byte[] encodedBytes = cipher.doFinal(etOrjText.getText().toString().trim().getBytes());
                //String encryptedBase64Encoded = Base64.encodeToString(encodedBytes, Base64.DEFAULT);

                System.out.println(" Java crypto encrypt text: >>>>" + encoderfun(encodedBytes));
                System.out.println("Android keystore encrypt text: >>>>" + encoderfun(cipherText));
                String sonuc = encoderfun(cipherText);
                tvSonuc.setText(sonuc);


                String tvIV = encoderfun(IV);
                //tvAnahtar.setText(tvIV);
                tvAnahtar.setText(encoderfun(encodedBytes));

            } catch (Exception e) {
                e.printStackTrace();
            }

        }
    }

    public static String encoderfun(byte[] decval) {
        String conVal= Base64.encodeToString(decval,Base64.DEFAULT);
        return conVal;
    }
}