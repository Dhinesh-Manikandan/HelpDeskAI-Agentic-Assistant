package com.helpdeskai.backend.entity;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
public class AgentExecution {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JsonIgnore
    private AgentTask task;
    
    @Enumerated(EnumType.STRING)
    private AgentState state;
    
    private String selectedTool;
    private String result;
    private LocalDateTime timestamp = LocalDateTime.now();
    private Long durationMs;
    public Long getId() { return this.id; }
    public void setId(Long id) { this.id = id; }
    public AgentTask getTask() { return this.task; }
    public void setTask(AgentTask task) { this.task = task; }
    public AgentState getState() { return this.state; }
    public void setState(AgentState state) { this.state = state; }
    public String getSelectedTool() { return this.selectedTool; }
    public void setSelectedTool(String selectedTool) { this.selectedTool = selectedTool; }
    public String getResult() { return this.result; }
    public void setResult(String result) { this.result = result; }
    public LocalDateTime getTimestamp() { return this.timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
    public Long getDurationMs() { return this.durationMs; }
    public void setDurationMs(Long durationMs) { this.durationMs = durationMs; }
}