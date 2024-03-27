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

        JPanel topPanel = new JPanel();
        topPanel.setBackground(Color.WHITE);
        topPanel.setPreferredSize(new Dimension(getWidth(), 100));
        add(topPanel, BorderLayout.NORTH);

        JLabel titleLabel = new JLabel("Multi-Tool App");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 24));
        topPanel.add(titleLabel);

        JPanel centerPanel = new JPanel(new GridBagLayout());
        centerPanel.setBackground(Color.WHITE);
        add(centerPanel, BorderLayout.CENTER);

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 10, 10);

        JButton ddosButton = new JButton("DDoS");
        stylizeButton(ddosButton);
        centerPanel.add(ddosButton, gbc);

        JButton bruteForceButton = new JButton("Brute Force");
        stylizeButton(bruteForceButton);
        gbc.gridx = 1;
        centerPanel.add(bruteForceButton, gbc);

        JButton ipToLocationButton = new JButton("IP to Location");
        stylizeButton(ipToLocationButton);
        gbc.gridx = 2;
        centerPanel.add(ipToLocationButton, gbc);

        JButton settingsButton = new JButton("Settings");
        stylizeButton(settingsButton);
        gbc.gridx = 3;
        centerPanel.add(settingsButton, gbc);

        settingsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle settings action
                JOptionPane.showMessageDialog(MultiToolApp.this, "Settings clicked!");
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
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click action
                JOptionPane.showMessageDialog(MultiToolApp.this, button.getText() + " clicked!");
            }
        });
    }

    public static void main(String[] args) {
        // Set the look and feel to Nimbus for modern UI
        try {
            UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
        } catch (Exception e) {
            e.printStackTrace();
        }

        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                MultiToolApp app = new MultiToolApp();
                app.setVisible(true);
            }
        });
    }
}
