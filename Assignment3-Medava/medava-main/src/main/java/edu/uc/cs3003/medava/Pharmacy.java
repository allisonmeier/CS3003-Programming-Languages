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
            System.out.println(String.format("Sending %s on the %s transporter.", advil.getMedicineName(),
                    t.getTransporterName()));
        } else {
            System.out.println(String.format("Cannot load %s on to the %s transporter.", advil.getMedicineName(),
                    t.getTransporterName()));
            return false;
        }

        Medicine activase = new Thrombolytic();
        if (t.load(activase)) {
            System.out.println(String.format("Sending %s on the %s transporter.", activase.getMedicineName(),
                    t.getTransporterName()));
        } else {
            System.out.println(String.format("Cannot load %s on to the %s transporter.", activase.getMedicineName(),
                    t.getTransporterName()));
            return false;
        }
        return true;
    }

    public String pharmacyName() {
        return mPharmacyName;
    }

}