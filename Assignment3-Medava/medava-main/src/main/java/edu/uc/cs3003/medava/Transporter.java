package edu.uc.cs3003.medava;
import java.util.List;
import java.util.ArrayList;

public class Transporter {

    // Declare vars
    private String mTransporterName;
    private List<Medicine> goods;
    private double mLowTemperature, mHighTemperature;
    {
        goods = new ArrayList<Medicine>();
    }

    // Constructor
    public Transporter(String transporterName, double lowTemp, double highTemp) {
        mTransporterName = transporterName;
        mLowTemperature = lowTemp;
        mHighTemperature = highTemp;
    }

    // Getter
    public String getTransporterName() {
        return mTransporterName;
    }

    // Methods
    public void ship() {
        // Do some shipping!
    }

    public boolean load(Medicine itemToLoad) {
        if (itemToLoad.isTemperatureRangeAcceptable(mLowTemperature, mHighTemperature)) {
            System.out.println(String.format("Adding a %s to the transporter.", itemToLoad.getMedicineName()));
            goods.add(itemToLoad);
            return true;
        }
        return false;
    }

    public Medicine unload() {
        return goods.remove(0);
    }
    public boolean isEmpty() {
        return goods.isEmpty();
    }

}