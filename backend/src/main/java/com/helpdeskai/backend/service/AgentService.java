package com.helpdeskai.backend.service;
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
                logState(task, AgentState.COMPLETED, null, "I am a specialized IT Support Agent. I can help you create tickets, close tickets, check your ticket status, and query the IT knowledge base. I am unable to fulfill this specific request.");
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
            
            if (selectedTool.equals("close_ticket")) {
                if (ticket1042Closed) {
                    logState(task, AgentState.COMPLETED, selectedTool, "I checked the system and Ticket #1042 is already resolved. No further action is required.");
                    task.setStatus("COMPLETED");
                    taskRepo.save(task);
                    return;
                }
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
    
    // Simple state for demo purposes to reflect dynamic changes
    private boolean ticket1042Closed = false;

    private void executeTool(AgentTask task, String toolName, User user) {
        logState(task, AgentState.EXECUTING, toolName, "Executing tool");
        try { Thread.sleep(1000); } catch(Exception ignored){}
        
        String result = "I have successfully executed the requested tool: " + toolName + ". Let me know if you need anything else.";
        
        if (toolName.equals("create_ticket")) {
            result = "I have created a high-priority ticket for your VPN issue. Your ticket number is #1050. Our IT support team has been notified and will reach out to you shortly.";
        }
        else if (toolName.equals("close_ticket")) {
            ticket1042Closed = true;
            result = "Ticket #1042 has been successfully closed. Please don't hesitate to reach out if you need any further assistance!";
        }
        else if (toolName.equals("get_my_tickets")) {
            if (ticket1042Closed) {
                result = "I found the following tickets under your account:\n\nOpen:\n(No open tickets)\n\nResolved:\n1) Ticket #1042: VPN not working\n2) Ticket #1021: Cannot access email\n\nIs there anything specific you would like me to do with these tickets?";
            } else {
                result = "I found the following tickets under your account:\n\nOpen:\n1) Ticket #1042: VPN not working\n\nResolved:\n1) Ticket #1021: Cannot access email\n\nIs there anything specific you would like me to do with these tickets?";
            }
        }
        else if (toolName.equals("get_ticket_status")) {
            if (ticket1042Closed) {
                result = "Ticket #1042 (VPN not working) is currently marked as RESOLVED. It was closed recently. Is there anything else you need help with?";
            } else {
                result = "Ticket #1042 (VPN not working) is currently OPEN. Our IT support team is actively investigating the issue.";
            }
        }
        else if (toolName.equals("search_knowledge")) {
            result = "Based on our knowledge base, you can reset your password by visiting the IT Self-Service Portal (https://it.company.com) and clicking on 'Forgot Password'. You will need to verify your identity using your secondary email or phone number.";
        }
        
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
        if (req.contains("reset") && req.contains("password")) return "search_knowledge";
        
        // If we don't understand the intent, return null to trigger the fallback message
        return null;
    }

    private void logState(AgentTask task, AgentState state, String tool, String result) {
        AgentExecution exec = new AgentExecution();
        exec.setTask(task);
        exec.setState(state);
        exec.setSelectedTool(tool);
        exec.setResult(result);
        execRepo.save(exec);
    }
}