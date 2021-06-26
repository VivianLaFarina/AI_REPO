package jorge.cardona.concepts.entity;

import jorge.cardona.concepts.adapter.annotations.properties.PropertyAnnotationValidationLenghtDescription;
import jorge.cardona.concepts.adapter.annotations.properties.PropertyAnotationValidatePropertyLenghtOther;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.*;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;
import java.sql.Timestamp;
import java.util.UUID;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "nature")
@Entity
public class NatureEntity {

    @Id
    @GeneratedValue(generator = "UUID")
    @GenericGenerator(
            name = "UUID",
            strategy = "org.hibernate.id.UUIDGenerator"
    )
    @Column(name = "id", updatable = false, unique = true, nullable = false)
    private UUID id;

    @NotNull
    @Column(name = "kingdom")
    @Size(min = 3, max = 10)
    @PropertyAnotationValidatePropertyLenghtOther(message = "the message was changed from original validator message... ")
    @NotBlank(message = "Name is mandatory")
    @Pattern(regexp = "^[\\p{Alnum}]{1,32}$")
    private String kingdom;

    @NotNull
    @PropertyAnnotationValidationLenghtDescription
    @Type(type="text")
    @Column(name = "description")
    private String description;

    @ColumnDefault("now()")
    @Type(type="timestamp")
    @CreationTimestamp
    @Column(name = "createDateTime")
    private Timestamp createDateTime;

    @ColumnDefault("now()")
    @Type(type="timestamp")
    @UpdateTimestamp
    @Column(name = "updateDateTime")
    private Timestamp updateDateTime;

}