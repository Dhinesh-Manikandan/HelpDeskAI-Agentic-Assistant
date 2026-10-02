package com.helpdeskai.backend.config;
import com.helpdeskai.backend.entity.*;
import com.helpdeskai.backend.repository.*;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class WebConfig {
    @Bean
    public CommandLineRunner initData(UserRepository userRepo, TicketRepository ticketRepo) {
        return args -> {
            if (userRepo.count() == 0) {
                User user = new User(); user.setUsername("demo_user"); user.setRole(User.Role.USER); userRepo.save(user);
                User agent = new User(); agent.setUsername("demo_agent"); agent.setRole(User.Role.SUPPORT_AGENT); userRepo.save(agent);
                User admin = new User(); admin.setUsername("demo_admin"); admin.setRole(User.Role.ADMIN); userRepo.save(admin);
                
                Ticket t1 = new Ticket(); t1.setTitle("VPN not working"); t1.setStatus("OPEN"); t1.setCreator(user); ticketRepo.save(t1);
                Ticket t2 = new Ticket(); t2.setTitle("Cannot access email"); t2.setStatus("RESOLVED"); t2.setCreator(user); ticketRepo.save(t2);
            }
        };
    }
}