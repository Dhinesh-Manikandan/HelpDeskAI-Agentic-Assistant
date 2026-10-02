import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/backend/src/main/java/com/helpdeskai/backend"

controllers = {
    "AgentController": """package com.helpdeskai.backend.controller;
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
}""",
    "DataController": """package com.helpdeskai.backend.controller;
import com.helpdeskai.backend.entity.*;
import com.helpdeskai.backend.repository.*;
import com.helpdeskai.backend.service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/data")
@CrossOrigin(origins = "*")
public class DataController {
    @Autowired private UserRepository userRepo;
    @Autowired private TicketRepository ticketRepo;
    @Autowired private ToolRegistry toolRegistry;
    @Autowired private ApprovalRepository approvalRepo;
    @Autowired private AuditLogRepository auditRepo;

    @GetMapping("/users")
    public List<User> getUsers() { return userRepo.findAll(); }

    @GetMapping("/tickets")
    public List<Ticket> getTickets() { return ticketRepo.findAll(); }
    
    @GetMapping("/tools")
    public List<Tool> getTools() { return toolRegistry.getAllTools(); }
    
    @GetMapping("/approvals")
    public List<Approval> getApprovals() { return approvalRepo.findAll(); }
    
    @GetMapping("/audit-logs")
    public List<AuditLog> getLogs() { return auditRepo.findAll(); }
}""",
    "Config": """package com.helpdeskai.backend.config;
import com.helpdeskai.backend.entity.*;
import com.helpdeskai.backend.repository.*;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class Config {
    @Bean
    public CommandLineRunner initData(UserRepository userRepo, TicketRepository ticketRepo) {
        return args -> {
            if (userRepo.count() == 0) {
                User user = new User(); user.setUsername("demo_user"); user.setRole(User.Role.USER); userRepo.save(user);
                User agent = new User(); agent.setUsername("demo_agent"); agent.setRole(User.Role.SUPPORT_AGENT); userRepo.save(agent);
                User admin = new User(); admin.setUsername("demo_admin"); admin.setRole(User.Role.ADMIN); userRepo.save(admin);
                
                Ticket t1 = new Ticket(); t1.setTitle("VPN not working"); t1.setStatus("OPEN"); t1.setCreator(user); ticketRepo.save(t1);
                Ticket t2 = new Ticket(); t2.setTitle("Cannot access email"); t2.setStatus("RESOLVED"); t2.setCreator(user); ticketRepo.save(t2);
            }
        };
    }
}"""
}

for name, content in controllers.items():
    if name == "Config":
        with open(os.path.join(base_dir, "config", "WebConfig.java"), "w") as f:
            f.write(content)
    else:
        with open(os.path.join(base_dir, "controller", f"{name}.java"), "w") as f:
            f.write(content)

print("Controllers created.")
