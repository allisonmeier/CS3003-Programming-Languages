package edu.uc.cs3003.medava;

public class Pharmacy {

    // Declare vars
    private String mPharmacyName;

    // Constructor
    public Pharmacy(String pharmacyName) {
        mPharmacyName = pharmacyName;
    }

    // Methods
    public boolean send(Transporter t) {
        Medicine advil = new Medicine("Advil");
        if (t.load(advil)) {
            System.out.println(String.format("Sending %s on the %s transporter.", advil.getMedicineName(), t.getTransporterName()));
            return true;
        }
        System.out.println(
                String.format("Cannot load %s on to the %s transporter.", advil.getMedicineName(), t.getTransporterName()));
        return false;
    }

    public String pharmacyName() {
        return mPharmacyName;
    }

}