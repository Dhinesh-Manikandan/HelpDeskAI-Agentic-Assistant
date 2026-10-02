package com.helpdeskai.backend.entity;
import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
public class AuditLog {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String action;
    @ManyToOne
    private User user;
    private String details;
    private LocalDateTime timestamp = LocalDateTime.now();
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getAction() { return this.action; }
    public void setAction(String action) { this.action = action; }
    public User getUser() { return this.user; }
    public void setUser(User user) { this.user = user; }
    public String getDetails() { return this.details; }
    public void setDetails(String details) { this.details = details; }
    public LocalDateTime getTimestamp() { return this.timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
}