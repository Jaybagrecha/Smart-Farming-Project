package com.harshvagh123.farm;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class Boundry extends AppCompatActivity {

    private Switch S;
    private TextView tv_pir;
    private boolean state;
    String temp;
    int x,x1;
    DatabaseReference ref = FirebaseDatabase.getInstance().getReference().child("Farm").child("Boundry");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_boundry);

                S = (Switch) findViewById(R.id.switch1);
        tv_pir = (TextView) findViewById(R.id.warning);

        ref.child("system").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                temp=snapshot.getValue().toString();
                x=Integer.parseInt(temp);
                if(x==1){
                    S.setChecked(true);
                    S.setText("SYSTEM ON         ");
                } else {
                    S.setChecked(false);
                    S.setText("SYSTEM OFF        ");
                }

            }
            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Boundry.this,"Error in Fetching Data",Toast.LENGTH_SHORT).show();
            }
        });

        ref.child("Detect").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                temp=snapshot.getValue().toString();
                x1=Integer.parseInt(temp);
                if(x1==1){
                    tv_pir.setText("Animal Detected");
                } else {
                    tv_pir.setText("S A F E");
                }
            }
            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Boundry.this,"Error in Fetching Data",Toast.LENGTH_SHORT).show();
            }
        });

        S.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                state = S.isChecked();

                if(state){
                    ref.child("system").setValue(1);
                    S.setText("SYSTEM ON         ");
                } else {
                    ref.child("system").setValue(0);
                    S.setText("SYSTEM OFF        ");
                }
            }
        });



    }
}
