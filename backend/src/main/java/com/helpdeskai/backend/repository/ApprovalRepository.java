package com.helpdeskai.backend.repository;
import com.helpdeskai.backend.entity.Approval;
import org.springframework.data.jpa.repository.JpaRepository;
public interface ApprovalRepository extends JpaRepository<Approval, Long> {
}