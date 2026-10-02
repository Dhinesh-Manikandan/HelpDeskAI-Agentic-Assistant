package com.helpdeskai.backend.controller;
import com.helpdeskai.backend.entity.*;
import com.helpdeskai.backend.repository.*;
import com.helpdeskai.backend.service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/agent")
@CrossOrigin(origins = "*")
public class AgentController {
    @Autowired private AgentService agentService;
    @Autowired private AgentTaskRepository taskRepo;
    @Autowired private AgentExecutionRepository execRepo;
    @Autowired private UserRepository userRepo;
    @Autowired private ApprovalRepository approvalRepo;

    @PostMapping("/request")
    public AgentTask submitRequest(@RequestBody Map<String, String> payload) {
        String request = payload.get("request");
        Long userId = Long.parseLong(payload.get("userId"));
        User user = userRepo.findById(userId).orElseThrow();
        return agentService.processRequest(request, user);
    }
    
    @GetMapping("/tasks/{id}")
    public AgentTask getTask(@PathVariable Long id) {
        return taskRepo.findById(id).orElseThrow();
    }
    
    @GetMapping("/tasks/{id}/executions")
    public List<AgentExecution> getExecutions(@PathVariable Long id) {
        return execRepo.findByTaskIdOrderByIdAsc(id);
    }
    
    @GetMapping("/tasks")
    public List<AgentTask> getAllTasks() {
        return taskRepo.findAll();
    }
    
    @PostMapping("/approvals/{id}/resolve")
    public Approval resolveApproval(@PathVariable Long id, @RequestBody Map<String, Object> payload) {
        Approval approval = approvalRepo.findById(id).orElseThrow();
        boolean approved = (Boolean) payload.get("approved");
        Long approverId = Long.parseLong(payload.get("approverId").toString());
        User approver = userRepo.findById(approverId).orElseThrow();
        
        approval.setStatus(approved ? "APPROVED" : "REJECTED");
        approval.setApprover(approver);
        approvalRepo.save(approval);
        
        // Find task associated (hack for demo: parse task ID from details)
        String details = approval.getActionDetails();
        Long taskId = Long.parseLong(details.substring(details.lastIndexOf(" ") + 1));
        
        agentService.resumeExecution(taskId, approved, approver);
        return approval;
    }
}