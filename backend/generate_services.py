import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/backend/src/main/java/com/helpdeskai/backend"

services = {
    "Tool": """package com.helpdeskai.backend.service;
import lombok.Data;
@Data
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
}""",
    "ToolRegistry": """package com.helpdeskai.backend.service;
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
}""",
    "AgentService": """package com.helpdeskai.backend.service;
import com.helpdeskai.backend.entity.*;
import com.helpdeskai.backend.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

@Service
public class AgentService {
    @Autowired private AgentTaskRepository taskRepo;
    @Autowired private AgentExecutionRepository execRepo;
    @Autowired private ToolRegistry toolRegistry;
    @Autowired private ApprovalRepository approvalRepo;
    @Autowired private AuditLogRepository auditRepo;

    public AgentTask processRequest(String request, User user) {
        AgentTask task = new AgentTask();
        task.setUserRequest(request);
        task.setUser(user);
        task.setStatus("ACTIVE");
        task = taskRepo.save(task);
        
        logState(task, AgentState.RECEIVED, null, "Received request");
        
        // Asynchronous processing to simulate agent thinking
        AgentTask finalTask = task;
        CompletableFuture.runAsync(() -> simulateAgentWorkflow(finalTask, request, user));
        
        return task;
    }
    
    private void simulateAgentWorkflow(AgentTask task, String request, User user) {
        try {
            logState(task, AgentState.ANALYZING, null, "Analyzing request intent");
            Thread.sleep(1000);
            
            logState(task, AgentState.PLANNING, null, "Planning execution steps");
            Thread.sleep(1000);
            
            String selectedTool = determineTool(request);
            if (selectedTool == null) {
                logState(task, AgentState.COMPLETED, null, "I couldn't understand the request. Please try again.");
                task.setStatus("COMPLETED");
                taskRepo.save(task);
                return;
            }
            
            Tool tool = toolRegistry.getTool(selectedTool);
            if (tool == null) {
                logState(task, AgentState.FAILED, null, "Tool not found");
                task.setStatus("FAILED");
                taskRepo.save(task);
                return;
            }
            
            if ("HIGH".equals(tool.getRiskLevel())) {
                logState(task, AgentState.WAITING_FOR_AUTHORIZATION, selectedTool, "Approval required for high risk action");
                Approval approval = new Approval();
                approval.setActionDetails("Execute " + selectedTool + " for task " + task.getId());
                approval.setRequester(user);
                approval.setStatus("PENDING");
                approvalRepo.save(approval);
                task.setStatus("WAITING");
                taskRepo.save(task);
                return;
            }
            
            executeTool(task, selectedTool, user);
            
        } catch (Exception e) {
            logState(task, AgentState.FAILED, null, "Error: " + e.getMessage());
            task.setStatus("FAILED");
            taskRepo.save(task);
        }
    }
    
    public void resumeExecution(Long taskId, boolean approved, User approver) {
        AgentTask task = taskRepo.findById(taskId).orElseThrow();
        if (approved) {
            String lastTool = execRepo.findByTaskIdOrderByIdDesc(taskId).get(0).getSelectedTool();
            executeTool(task, lastTool, task.getUser());
        } else {
            logState(task, AgentState.CANCELLED, null, "Action rejected by admin");
            task.setStatus("CANCELLED");
            taskRepo.save(task);
        }
    }
    
    private void executeTool(AgentTask task, String toolName, User user) {
        logState(task, AgentState.EXECUTING, toolName, "Executing tool");
        try { Thread.sleep(1000); } catch(Exception ignored){}
        
        String result = "Executed " + toolName + " successfully";
        if (toolName.equals("create_ticket")) result = "Ticket #1050 created.";
        if (toolName.equals("close_ticket")) result = "Ticket closed.";
        
        logState(task, AgentState.VALIDATING, toolName, "Validating results");
        try { Thread.sleep(500); } catch(Exception ignored){}
        
        logState(task, AgentState.COMPLETED, toolName, result);
        task.setStatus("COMPLETED");
        taskRepo.save(task);
        
        AuditLog auditLog = new AuditLog();
        auditLog.setAction("TOOL_EXECUTION");
        auditLog.setUser(user);
        auditLog.setDetails("Executed " + toolName + " for task " + task.getId());
        auditRepo.save(auditLog);
    }
    
    private String determineTool(String request) {
        String req = request.toLowerCase();
        if (req.contains("create") && req.contains("ticket")) return "create_ticket";
        if (req.contains("close") && req.contains("ticket")) return "close_ticket";
        if (req.contains("my tickets") || req.contains("open tickets")) return "get_my_tickets";
        if (req.contains("status")) return "get_ticket_status";
        if (req.contains("health")) return "get_system_health";
        if (req.contains("search") || req.contains("how do i") || req.contains("password")) return "search_knowledge";
        return "search_knowledge";
    }

    private void logState(AgentTask task, AgentState state, String tool, String result) {
        AgentExecution exec = new AgentExecution();
        exec.setTask(task);
        exec.setState(state);
        exec.setSelectedTool(tool);
        exec.setResult(result);
        execRepo.save(exec);
    }
}"""
}

# Need a custom method in AgentExecutionRepository
execution_repo = """package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.AgentExecution;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
public interface AgentExecutionRepository extends JpaRepository<AgentExecution, Long> {
    List<AgentExecution> findByTaskIdOrderByIdDesc(Long taskId);
    List<AgentExecution> findByTaskIdOrderByIdAsc(Long taskId);
}"""

for name, content in services.items():
    with open(os.path.join(base_dir, "service", f"{name}.java"), "w") as f:
        f.write(content)

with open(os.path.join(base_dir, "repository", "AgentExecutionRepository.java"), "w") as f:
    f.write(execution_repo)
    
print("Services created.")
