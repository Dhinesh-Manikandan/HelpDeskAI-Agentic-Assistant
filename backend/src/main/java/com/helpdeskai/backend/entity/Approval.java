package com.helpdeskai.backend.entity;
import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
public class Approval {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String actionDetails;
    private String status; // PENDING, APPROVED, REJECTED
    @ManyToOne
    private User requester;
    @ManyToOne
    private User approver;
    private LocalDateTime requestedAt = LocalDateTime.now();
    private LocalDateTime resolvedAt;
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getActionDetails() { return this.actionDetails; }
    public void setActionDetails(String actionDetails) { this.actionDetails = actionDetails; }
    public String getStatus() { return this.status; }
    public void setStatus(String status) { this.status = status; }
    public User getRequester() { return this.requester; }
    public void setRequester(User requester) { this.requester = requester; }
    public User getApprover() { return this.approver; }
    public void setApprover(User approver) { this.approver = approver; }
    public LocalDateTime getRequestedAt() { return this.requestedAt; }
    public void setRequestedAt(LocalDateTime requestedAt) { this.requestedAt = requestedAt; }
    public LocalDateTime getResolvedAt() { return this.resolvedAt; }
    public void setResolvedAt(LocalDateTime resolvedAt) { this.resolvedAt = resolvedAt; }
}