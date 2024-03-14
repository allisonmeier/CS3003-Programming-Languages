package edu.uc.cs3003.medava;
import java.util.List;
import java.util.ArrayList;

public class Transporter {

    // Declare vars
    private String mTransporterName;
    public List<Medicine> goods;
    {
        goods = new ArrayList<Medicine>();
    }

    // Getter
    public String getTransporterName() {
        return mTransporterName;
    }

    // Methods
    public void ship() {
        // Do some shipping!
    }

}