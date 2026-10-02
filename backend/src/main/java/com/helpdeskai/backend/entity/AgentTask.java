package com.helpdeskai.backend.entity;
import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.List;

@Entity
public class AgentTask {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String userRequest;
    private String status; // ACTIVE, COMPLETED, FAILED
    @ManyToOne
    private User user;
    private LocalDateTime createdAt = LocalDateTime.now();
    
    @OneToMany(mappedBy = "task", cascade = CascadeType.ALL)
    private List<AgentExecution> executions;
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getUserRequest() { return this.userRequest; }
    public void setUserRequest(String userRequest) { this.userRequest = userRequest; }
    public String getStatus() { return this.status; }
    public void setStatus(String status) { this.status = status; }
    public User getUser() { return this.user; }
    public void setUser(User user) { this.user = user; }
    public LocalDateTime getCreatedAt() { return this.createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public List<AgentExecution> getExecutions() { return this.executions; }
    public void setExecutions(List<AgentExecution> executions) { this.executions = executions; }
}