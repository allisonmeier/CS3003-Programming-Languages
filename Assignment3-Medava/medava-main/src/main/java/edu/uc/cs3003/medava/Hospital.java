package edu.uc.cs3003.medava;

public class Hospital {

    // Declare vars
    private String name;

    // Constructor
    public Hospital(String hospitalName) {
        name = hospitalName;
    }

    // Methods
    void receive(Transporter t) {
        while (!t.isEmpty()) {
            Medicine unloaded = t.unload();
            System.out.println(String.format("Receiving %s off the %s transporter.", unloaded.getMedicineName(), t.getTransporterName()));
        }
    }

    public String name() {
        return name;
    }

}
