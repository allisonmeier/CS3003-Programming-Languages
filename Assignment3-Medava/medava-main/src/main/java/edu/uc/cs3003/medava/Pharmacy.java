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
        System.out.println(String.format("Sending an %s.", advil.getMedicineName()));
        return t.goods.add(advil);
    }

    public String pharmacyName() {
        return mPharmacyName;
    }

}