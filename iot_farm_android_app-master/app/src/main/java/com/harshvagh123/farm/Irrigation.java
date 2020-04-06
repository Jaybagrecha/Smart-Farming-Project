package com.harshvagh123.farm;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ProgressBar;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class Irrigation extends AppCompatActivity {

    private TextView tv_water;
    private Switch S;
    private ProgressBar progressBar;
    private boolean state;
    private String s_level,s_moist;
    private float per;
    private int x1,x2;
    String temp;
    int a;

    DatabaseReference ref = FirebaseDatabase.getInstance().getReference().child("Farm").child("Irrigation");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_irrigation);


        tv_water = (TextView) findViewById(R.id.water);
        S = (Switch) findViewById(R.id.switch1);



        ref.child("Moisture").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                s_moist=snapshot.getValue().toString();
                x2=Integer.parseInt(s_moist);
                if(x2==1){
                    tv_water.setText("Water Detected");
                } else {
                    tv_water.setText("No Water Detected");
                }

            }
            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Irrigation.this,"Error in Fetching Data",Toast.LENGTH_SHORT).show();
            }
        });

        ref.child("system").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                temp=snapshot.getValue().toString();
                a=Integer.parseInt(temp);
                if(a==1){
                    S.setChecked(true);
                    S.setText("IRRIGATION ON      ");
                } else {
                    S.setChecked(false);
                    S.setText("IRRIGATION OFF     ");
                }

            }
            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Irrigation.this,"Error in Fetching Data",Toast.LENGTH_SHORT).show();
            }
        });


        S.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                state = S.isChecked();

                if(state){
                    ref.child("system").setValue(1);
                    S.setText("IRRIGATION ON      ");

                } else {
                    ref.child("system").setValue(0);
                    S.setText("IRRIGATION OFF     ");
                }

            }
        });



    }
}
