import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MultiToolApp extends JFrame {
    public MultiToolApp() {
        setTitle("Multi-Tool App");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        topPanel.setBackground(Color.WHITE);
        topPanel.setPreferredSize(new Dimension(getWidth(), 100));
        add(topPanel, BorderLayout.NORTH);

        JButton ddosButton = new JButton("DDoS");
        stylizeButton(ddosButton);
        topPanel.add(ddosButton);

        JButton bruteForceButton = new JButton("Brute Force");
        stylizeButton(bruteForceButton);
        topPanel.add(bruteForceButton);

        JButton ipToLocationButton = new JButton("IP to Location");
        stylizeButton(ipToLocationButton);
        topPanel.add(ipToLocationButton);

        JButton settingsButton = new JButton("Settings");
        stylizeButton(settingsButton);
        topPanel.add(settingsButton);

        settingsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle settings action
            }
        });
    }

    private void stylizeButton(JButton button) {
        button.setPreferredSize(new Dimension(150, 50));
        button.setBackground(Color.WHITE);
        button.setForeground(Color.BLACK);
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        button.setFont(new Font("Arial", Font.PLAIN, 16));
    }

    public static void main(String[] args) {
        // Set the look and feel to Nimbus 
