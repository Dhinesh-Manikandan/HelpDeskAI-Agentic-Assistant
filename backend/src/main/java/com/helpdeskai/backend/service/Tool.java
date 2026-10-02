package com.helpdeskai.backend.service;


public class Tool {
    private String name;
    private String description;
    private String riskLevel; // LOW, MEDIUM, HIGH
    private String requiredRole;
    private boolean enabled;
    
    public Tool(String name, String description, String riskLevel, String requiredRole, boolean enabled) {
        this.name = name;
        this.description = description;
        this.riskLevel = riskLevel;
        this.requiredRole = requiredRole;
        this.enabled = enabled;
    }
    public String getName() { return this.name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return this.description; }
    public void setDescription(String description) { this.description = description; }
    public String getRiskLevel() { return this.riskLevel; }
    public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }
    public String getRequiredRole() { return this.requiredRole; }
    public void setRequiredRole(String requiredRole) { this.requiredRole = requiredRole; }
    public boolean getEnabled() { return this.enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}