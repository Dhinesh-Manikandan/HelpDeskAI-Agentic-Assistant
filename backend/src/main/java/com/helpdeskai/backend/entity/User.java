package com.helpdeskai.backend.entity;
import jakarta.persistence.*;


@Entity
@Table(name = "users")
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String email;
    @Enumerated(EnumType.STRING)
    private Role role;
    public enum Role { USER, SUPPORT_AGENT, ADMIN }
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getUsername() { return this.username; }
    public void setUsername(String username) { this.username = username; }
    public String getEmail() { return this.email; }
    public void setEmail(String email) { this.email = email; }
    public Role getRole() { return this.role; }
    public void setRole(Role role) { this.role = role; }
}