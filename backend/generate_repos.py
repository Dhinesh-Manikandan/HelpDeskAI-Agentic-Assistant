import os

base_dir = "d:/Sem VII/IOC/Assignment/Application/HelpDeskAI-Agentic-Assistant/backend/src/main/java/com/helpdeskai/backend"

# Generate Repositories
repos = ["User", "Ticket", "KnowledgeArticle", "AgentTask", "AgentExecution", "ToolExecution", "Approval", "AuditLog"]
for repo in repos:
    content = f"""package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.{repo};
import org.springframework.data.jpa.repository.JpaRepository;
public interface {repo}Repository extends JpaRepository<{repo}, Long> {{
}}"""
    with open(os.path.join(base_dir, "repository", f"{repo}Repository.java"), "w") as f:
        f.write(content)

# Specific repositories methods
user_repo_content = """package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}"""
with open(os.path.join(base_dir, "repository", "UserRepository.java"), "w") as f:
    f.write(user_repo_content)

ticket_repo_content = """package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.Ticket;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
public interface TicketRepository extends JpaRepository<Ticket, Long> {
    List<Ticket> findByCreatorId(Long creatorId);
}"""
with open(os.path.join(base_dir, "repository", "TicketRepository.java"), "w") as f:
    f.write(ticket_repo_content)


print("Repos created.")
