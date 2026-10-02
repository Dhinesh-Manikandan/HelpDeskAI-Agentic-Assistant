package com.helpdeskai.backend.controller;
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
}