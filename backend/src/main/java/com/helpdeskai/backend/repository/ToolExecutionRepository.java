package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.ToolExecution;
import org.springframework.data.jpa.repository.JpaRepository;
public interface ToolExecutionRepository extends JpaRepository<ToolExecution, Long> {
}