package com.helpdeskai.backend.entity;
import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
public class ToolExecution {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String toolName;
    private String riskLevel; // LOW, MEDIUM, HIGH
    private String status; // SUCCESS, FAILED
    private String input;
    private String output;
    private Integer retryCount = 0;
    private LocalDateTime timestamp = LocalDateTime.now();
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public String getToolName() { return this.toolName; }
    public void setToolName(String toolName) { this.toolName = toolName; }
    public String getRiskLevel() { return this.riskLevel; }
    public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }
    public String getStatus() { return this.status; }
    public void setStatus(String status) { this.status = status; }
    public String getInput() { return this.input; }
    public void setInput(String input) { this.input = input; }
    public String getOutput() { return this.output; }
    public void setOutput(String output) { this.output = output; }
    public Integer getRetryCount() { return this.retryCount; }
    public void setRetryCount(Integer retryCount) { this.retryCount = retryCount; }
    public LocalDateTime getTimestamp() { return this.timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
}