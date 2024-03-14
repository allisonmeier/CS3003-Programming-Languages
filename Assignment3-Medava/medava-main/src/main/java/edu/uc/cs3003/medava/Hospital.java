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
        while (!t.goods.isEmpty()) {
            Medicine unloaded = t.goods.remove(0);
            System.out.println(String.format("Receiving an %s.", unloaded.getMedicineName()));
        }
    }

    public String name() {
        return name;
    }

}
