import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/backend/src/main/java/com/helpdeskai/backend"
dirs = [
    "entity", "repository", "service", "controller", "dto", "config", "enums"
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# Generate Entities
entities = {
    "User": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
@Data
@Entity
@Table(name = "users")
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String email;
    @Enumerated(EnumType.STRING)
    private Role role;
    public enum Role { USER, SUPPORT_AGENT, ADMIN }
}""",
    "Ticket": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
@Data
@Entity
public class Ticket {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String description;
    private String status; // OPEN, IN_PROGRESS, RESOLVED, CLOSED
    private String priority; // LOW, MEDIUM, HIGH
    @ManyToOne
    private User creator;
    @ManyToOne
    private User assignee;
    private LocalDateTime createdAt = LocalDateTime.now();
    private LocalDateTime updatedAt = LocalDateTime.now();
}""",
    "KnowledgeArticle": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
@Data
@Entity
public class KnowledgeArticle {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    @Column(columnDefinition = "TEXT")
    private String content;
    private String tags;
}""",
    "AgentTask": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;
@Data
@Entity
public class AgentTask {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String userRequest;
    private String status; // ACTIVE, COMPLETED, FAILED
    @ManyToOne
    private User user;
    private LocalDateTime createdAt = LocalDateTime.now();
    
    @OneToMany(mappedBy = "task", cascade = CascadeType.ALL)
    private List<AgentExecution> executions;
}""",
    "AgentExecution": """package com.helpdeskai.backend.entity;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
@Data
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
}""",
    "AgentState": """package com.helpdeskai.backend.entity;
public enum AgentState {
    IDLE, RECEIVED, ANALYZING, PLANNING, WAITING_FOR_AUTHORIZATION, EXECUTING, VALIDATING, RETRYING, COMPLETED, FAILED, CANCELLED
}""",
    "ToolExecution": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
@Data
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
}""",
    "Approval": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
@Data
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
}""",
    "AuditLog": """package com.helpdeskai.backend.entity;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
@Data
@Entity
public class AuditLog {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String action;
    @ManyToOne
    private User user;
    private String details;
    private LocalDateTime timestamp = LocalDateTime.now();
}"""
}

for name, content in entities.items():
    with open(os.path.join(base_dir, "entity", f"{name}.java"), "w") as f:
        f.write(content)

print("Entities created successfully.")
