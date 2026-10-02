package com.helpdeskai.backend.service;
import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

@Service
public class ToolRegistry {
    private final Map<String, Tool> tools = new HashMap<>();

    public ToolRegistry() {
        registerTool(new Tool("search_knowledge", "Search knowledge base", "LOW", "USER", true));
        registerTool(new Tool("create_ticket", "Create a support ticket", "LOW", "USER", true));
        registerTool(new Tool("get_my_tickets", "Get user's tickets", "LOW", "USER", true));
        registerTool(new Tool("get_ticket_status", "Get ticket status", "LOW", "USER", true));
        registerTool(new Tool("update_ticket", "Update a ticket", "MEDIUM", "USER", true));
        registerTool(new Tool("resolve_ticket", "Resolve a ticket", "MEDIUM", "SUPPORT_AGENT", true));
        registerTool(new Tool("close_ticket", "Close a ticket", "HIGH", "ADMIN", true));
        registerTool(new Tool("get_system_health", "Get system health", "LOW", "ADMIN", true));
    }

    public void registerTool(Tool tool) {
        tools.put(tool.getName(), tool);
    }

    public Tool getTool(String name) {
        return tools.get(name);
    }
    
    public List<Tool> getAllTools() {
        return new ArrayList<>(tools.values());
    }
}