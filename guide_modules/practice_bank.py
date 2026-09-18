# -*- coding: utf-8 -*-
"""Mega NPTEL Exam Practice Question Bank Module (MCQ & MSQ)"""

def get_practice_bank_content():
    return """
        <!-- ============================================================ -->
        <!-- MEGA NPTEL EXAM PRACTICE QUESTION BANK (MCQ & MSQ) -->
        <!-- ============================================================ -->
        <article class="week-module" id="mega-exam-question-bank" style="border-top: 5px solid #8b5cf6;">
            <header class="week-header" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);">
                <div class="week-tag" style="background: #ede9fe; color: #5b21b6;">Official NPTEL Format</div>
                <h2 class="week-title" style="color: #ffffff;">🏆 Mega NPTEL Exam Practice Question Bank (MCQ &amp; MSQ)</h2>
                <p class="week-desc" style="color: #c7d2fe;">
                    Comprehensive, exam-simulated question bank mirroring the official NPTEL certification exam pattern. Features rigorous <strong>Single-Choice MCQs (1–2 Marks)</strong> and high-stakes <strong>Multiple-Select MSQs (1 or More Options Correct, No Partial Marking)</strong> spanning Weeks 1 through 8, complete with full mathematical derivations and comprehensive distractor analyses.
                </p>
                <div style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 10px; font-size: 0.8rem; color: #e0e7ff;">
                    <span style="background: rgba(255,255,255,0.15); padding: 4px 10px; border-radius: 4px;">🎯 <strong>Format:</strong> 16 High-Yield Exam Questions (8 MCQs + 8 MSQs)</span>
                    <span style="background: rgba(255,255,255,0.15); padding: 4px 10px; border-radius: 4px;">⚖️ <strong>MSQ Rule:</strong> All correct options must be selected; zero marks for partial answers</span>
                    <span style="background: rgba(255,255,255,0.15); padding: 4px 10px; border-radius: 4px;">⏱️ <strong>Recommended Time:</strong> 60–75 Minutes</span>
                </div>
            </header>

            <div class="module-body">
                <div class="callout callout-warning" style="margin-bottom: 24px;">
                    <div class="callout-title">⚠️ NPTEL Certification Exam Instructions (Read Before Solving)</div>
                    <p style="margin: 0; font-size: 0.88rem; line-height: 1.55;">
                        • <strong>MCQ (Multiple Choice Questions):</strong> Exactly ONE option is correct. Negative marking of 25% or 33% may apply in certain test sessions.<br>
                        • <strong>MSQ (Multiple Select Questions):</strong> ONE OR MORE options can be correct (from 1 to 4). There is <strong>NO PARTIAL MARKING</strong> and typically no negative marking. You will receive credit if and only if you select all correct options and none of the incorrect ones.<br>
                        • Click any question drawer below to inspect the complete step-by-step mathematical solution and detailed distractor analysis!
                    </p>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 1 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 1</span>
                        R Programming, Data Structures &amp; Manipulation
                    </h3>
                </div>

                <!-- W1 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q1">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 1 • [1 Mark]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: String Concatenation &amp; Vector Recycling</span>
                    </div>
                    <div class="question-body">
                        <p>Consider the following R code snippet executed in a fresh R console:</p>
                        <pre class="r-code">x &lt;- c("A", "B")
y &lt;- c(1, 2, 3, 4)
res &lt;- paste(x, y, sep = "-", collapse = ";")</pre>
                        <p>What will be the output of <code class="inline-code">nchar(res)</code> and the value stored in <code class="inline-code">res</code>?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> <code class="inline-code">res</code> is a vector of length 4: <code class="inline-code">c("A-1", "B-2", "A-3", "B-4")</code> with <code class="inline-code">nchar(res) = c(3, 3, 3, 3)</code></li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> <code class="inline-code">res</code> is a single string: <code class="inline-code">"A-1;B-2;A-3;B-4"</code> with <code class="inline-code">nchar(res) = 15</code></li>
                            <li><span class="opt-bullet">(C)</span> <code class="inline-code">res</code> is a single string: <code class="inline-code">"A-1-B-2-A-3-B-4"</code> with <code class="inline-code">nchar(res) = 15</code></li>
                            <li><span class="opt-bullet">(D)</span> An error is thrown because <code class="inline-code">length(x)</code> does not match <code class="inline-code">length(y)</code></li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Vector Recycling Mechanism</div>
                                <p>Vector <code class="inline-code">x</code> has length 2 and <code class="inline-code">y</code> has length 4. In R, because 4 is an exact multiple of 2 ($4 = 2 \times 2$), <code class="inline-code">x</code> is recycled silently without warnings to match length 4: <code class="inline-code">c("A", "B", "A", "B")</code>.</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Element-wise Separator (<code class="inline-code">sep = "-"</code>)</div>
                                <p>Pairing elements with separator <code class="inline-code">"-"</code> creates an intermediate character vector of length 4:<br>
                                <code class="inline-code">c("A-1", "B-2", "A-3", "B-4")</code>.</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Vector-to-Scalar Collapse (<code class="inline-code">collapse = ";"</code>)</div>
                                <p>Because <code class="inline-code">collapse = ";"</code> is supplied, all elements of the resulting character vector are joined together with semicolons into a single scalar string:<br>
                                <code class="inline-code">"A-1;B-2;A-3;B-4"</code>.<br>
                                Counting characters: 4 letters ('A','B','A','B') + 4 hyphens + 4 digits ('1','2','3','4') + 3 semicolons = $4 + 4 + 4 + 3 = 15$ characters.</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Distractor Breakdown</div>
                                <p>• <strong>(A) is FALSE:</strong> If <code class="inline-code">collapse</code> were omitted, the result would be a vector of length 4. But <code class="inline-code">collapse = ";"</code> collapses it into length 1.<br>
                                • <strong>(C) is FALSE:</strong> Semicolons separate the recycled pairs, not hyphens.<br>
                                • <strong>(D) is FALSE:</strong> R automatically recycles when the longer length is an integer multiple of the shorter length.</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) "A-1;B-2;A-3;B-4" with nchar = 15</div>
                        </div>
                    </details>
                </div>

                <!-- W1 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q2">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 2 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: R Data Structures &amp; Type Coercion</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding R programming data structures and behavior? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> A matrix in R is stored internally as a vector with a <code class="inline-code">dim</code> attribute, and can hold elements of only ONE atomic data type.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> Evaluating <code class="inline-code">c(TRUE, 2L, 3.5, "apple")</code> results in a character vector due to R's implicit coercion hierarchy: <code class="inline-code">logical -&gt; integer -&gt; double -&gt; character</code>.</li>
                            <li><span class="opt-bullet">[C]</span> A data frame requires all of its columns to have the exact same data type, similar to a 2D matrix.</li>
                            <li class="correct-option"><span class="opt-bullet">[D]</span> In a boxplot produced by <code class="inline-code">boxplot()</code>, any data point outside the interval $[Q_1 - 1.5 \\times \\text{IQR}, \\; Q_3 + 1.5 \\times \\text{IQR}]$ is classified and plotted as an outlier.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> In R, a matrix is simply an atomic vector with a dimension attribute (<code class="inline-code">dim</code>). Because it is atomic, all elements must share the identical type.<br>
                                • <strong>[B] is TRUE:</strong> The coercion order is strictly <code class="inline-code">logical &lt; integer &lt; double &lt; character</code>. The presence of <code class="inline-code">"apple"</code> forces every element to coerce to character.<br>
                                • <strong>[C] is FALSE:</strong> A data frame is a heterogeneous structure (technically a list of equal-length vectors), meaning different columns can hold different types (e.g. numeric, factor, character).<br>
                                • <strong>[D] is TRUE:</strong> By Tukey's standard boxplot rule used in NPTEL and R, the upper fence is $Q_3 + 1.5 \\times \\text{IQR}$ and the lower fence is $Q_1 - 1.5 \\times \\text{IQR}$. Any observation beyond these fences is rendered as an individual outlier point.</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [D]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 2 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 2</span>
                        Linear Algebra, Hyperplanes, Pseudoinverses &amp; Eigenvalues
                    </h3>
                </div>

                <!-- W2 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q3">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 3 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: Point-to-Hyperplane Perpendicular Distance</span>
                    </div>
                    <div class="question-body">
                        <p>Consider a hyperplane $H$ in $\\mathbb{R}^3$ defined by the equation:</p>
                        $$2x_1 - 2x_2 + x_3 - 6 = 0$$
                        <p>What is the shortest perpendicular Euclidean distance from the point $x_0 = [1, \\; -1, \\; 2]^T$ to this hyperplane?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> $d = 1.0$</li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> $d = 0.0$ ($x_0$ lies exactly on the hyperplane)</li>
                            <li><span class="opt-bullet">(C)</span> $d = 2.0$</li>
                            <li><span class="opt-bullet">(D)</span> $d = \\frac{4}{3}$</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Identify Normal Vector $w$ and Bias $b$</div>
                                <p>From the hyperplane equation $w^T x + b = 0$:<br>
                                Normal vector $w = [2, \\; -2, \\; 1]^T$ and $b = -6$.</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Compute Euclidean Norm $\|w\|_2$</div>
                                <p>$$\|w\|_2 = \\sqrt{2^2 + (-2)^2 + 1^2} = \\sqrt{4 + 4 + 1} = \\sqrt{9} = 3$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Evaluate Point in Hyperplane Equation</div>
                                <p>Substitute $x_0 = [1, \\; -1, \\; 2]^T$ into the numerator:<br>
                                $$w^T x_0 + b = 2(1) - 2(-1) + 1(2) - 6 = 2 + 2 + 2 - 6 = 0$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 4: Compute Distance $d$</div>
                                <p>$$d = \\frac{|w^T x_0 + b|}{\|w\|_2} = \\frac{|0|}{3} = 0$$<br>
                                Because $w^T x_0 + b = 0$, the point satisfies the hyperplane equation identically, meaning it lies directly on the hyperplane!</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) d = 0.0 (x_0 lies on the hyperplane)</div>
                        </div>
                    </details>
                </div>

                <!-- W2 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q4">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 4 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: Linear Systems, Pseudoinverses &amp; Eigenvalues</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding linear systems, pseudoinverses, and eigenvalues? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> For an overdetermined system $Ax = b$ with $A \\in \\mathbb{R}^{m \\times n}$ ($m &gt; n$) having full column rank, the left Moore-Penrose pseudoinverse is $A^+ = (A^T A)^{-1} A^T$, which minimizes the sum of squared residuals $\|Ax - b\|_2^2$.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> For any non-zero column vector $u \\in \\mathbb{R}^n$ ($n \\ge 3$), the outer product matrix $M = u u^T$ has rank 1, exactly one non-zero eigenvalue $\\lambda_1 = \|u\|_2^2$, and the sum of products of eigenvalues taken two at a time is strictly 0.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> If $\\lambda$ is an eigenvalue of an invertible matrix $A$, then $\\frac{1}{\\lambda}$ is an eigenvalue of $A^{-1}$, and $\\det(A^{-1}) = \\det((A^{-1})^T) = \\frac{1}{\\det(A)}$.</li>
                            <li><span class="opt-bullet">[D]</span> An underdetermined linear system $Ax = b$ with $m &lt; n$ can have a unique solution if $\\text{rank}(A) = m$.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> When $m &gt; n$ with full column rank, $A^T A$ is $n \\times n$ and invertible. The unique least-squares solution is $\\hat{x} = (A^T A)^{-1} A^T b$.<br>
                                • <strong>[B] is TRUE:</strong> $M u = (u u^T) u = u (u^T u) = (\|u\|_2^2) u$, so $\\lambda_1 = \|u\|_2^2$. Since $\\text{rank}(M) = 1$, all remaining $n-1$ eigenvalues are 0. Thus, in any product of two eigenvalues $\\lambda_i \\lambda_j$ with $i \\neq j$, at least one factor is 0, making the sum identically 0.<br>
                                • <strong>[C] is TRUE:</strong> $A v = \\lambda v \\implies A^{-1} v = \\frac{1}{\\lambda} v$. Also, $\\det(A^{-1}) = 1/\\det(A)$, and transposing does not change the determinant: $\\det(M^T) = \\det(M)$.<br>
                                • <strong>[D] is FALSE:</strong> An underdetermined system ($m &lt; n$) can NEVER have a unique solution! It has either no solution (if inconsistent) or infinitely many solutions with $n - r$ free variables.</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 3 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 3</span>
                        Probability Distributions, Bayes' Theorem &amp; Hypothesis Testing
                    </h3>
                </div>

                <!-- W3 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q5">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 5 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: Bayes' Theorem &amp; Total Probability</span>
                    </div>
                    <div class="question-body">
                        <p>A manufacturing plant receives microchips from two suppliers: Supplier $S_1$ provides 60% of all chips, and Supplier $S_2$ provides the remaining 40%. Historically, 2% of chips from $S_1$ are defective, whereas 5% of chips from $S_2$ are defective. A chip is selected at random from the assembly line and found to be defective ($D$). What is the posterior probability $P(S_1 \mid D)$ that this defective chip came from Supplier $S_1$?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> 0.6000</li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> 0.3750</li>
                            <li><span class="opt-bullet">(C)</span> 0.6250</li>
                            <li><span class="opt-bullet">(D)</span> 0.0120</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Define Prior Probabilities &amp; Likelihoods</div>
                                <p>• $P(S_1) = 0.60, \\quad P(S_2) = 0.40$<br>
                                • $P(D \mid S_1) = 0.02, \\quad P(D \mid S_2) = 0.05$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Compute Total Probability of a Defect $P(D)$</div>
                                <p>$$P(D) = P(D \mid S_1)P(S_1) + P(D \mid S_2)P(S_2)$$
                                $$P(D) = (0.02 \\times 0.60) + (0.05 \\times 0.40) = 0.0120 + 0.0200 = 0.0320$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Apply Bayes' Theorem</div>
                                <p>$$P(S_1 \mid D) = \\frac{P(D \mid S_1)P(S_1)}{P(D)} = \\frac{0.0120}{0.0320} = \\frac{12}{32} = \\frac{3}{8} = 0.3750$$</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) 0.3750 (or 37.5%)</div>
                        </div>
                    </details>
                </div>

                <!-- W3 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q6">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 6 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: Sampling Distributions &amp; Hypothesis Testing</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding probability distributions, sampling statistics, and hypothesis testing? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> For nominal/categorical data (e.g. eye color, machine brand), the mode is the ONLY meaningful measure of central tendency; the arithmetic mean and median are undefined.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> When drawing a sample of size $n$ without replacement from a finite population of size $N$ containing $K$ successes, the exact number of successes follows a Hypergeometric distribution, not a Binomial distribution.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> If a random sample of size $n$ is drawn from a normal distribution $N(\\mu, \\sigma^2)$, the scaled sample variance $\\frac{(n-1)s^2}{\\sigma^2}$ follows a Chi-Square distribution with $n-1$ degrees of freedom.</li>
                            <li><span class="opt-bullet">[D]</span> In hypothesis testing, the probability of committing a Type I error ($\\alpha$) is equal to $1 - \\text{Power of the test}$.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> Categorical data has no natural numerical ordering or distance, making arithmetic averages meaningless. The mode (most frequent category) is the sole valid measure of central tendency.<br>
                                • <strong>[B] is TRUE:</strong> Sampling without replacement alters the trial probability dynamically, which is the foundational definition of the Hypergeometric distribution.<br>
                                • <strong>[C] is TRUE:</strong> A fundamental statistical theorem taught in Week 3 Lecture 21: $\\sum_{i=1}^n \\frac{(X_i - \\bar{X})^2}{\\sigma^2} = \\frac{(n-1)s^2}{\\sigma^2} \\sim \\chi^2(n-1)$.<br>
                                • <strong>[D] is FALSE:</strong> The power of a test is defined as $1 - \\beta$, where $\\beta$ is the probability of a Type II error (NOT Type I error $\\alpha$).</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 4 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 4</span>
                        Univariate Optimization, Numerical Methods &amp; Convexity
                    </h3>
                </div>

                <!-- W4 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q7">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 7 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: Newton-Raphson Optimization Step</span>
                    </div>
                    <div class="question-body">
                        <p>We wish to find the local unconstrained minimum of the function $f(x) = x^4 - 6x^2 + 4x + 10$ using the Newton-Raphson optimization method. Starting from an initial guess $x_0 = 2.0$, what is the next iterate $x_1$?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> $x_1 = 2.00$</li>
                            <li><span class="opt-bullet">(B)</span> $x_1 = 1.25$</li>
                            <li class="correct-option"><span class="opt-bullet">(C)</span> $x_1 = 1.6667$ ($5/3$)</li>
                            <li><span class="opt-bullet">(D)</span> $x_1 = 2.3333$</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Compute First and Second Derivatives</div>
                                <p>• $f'(x) = 4x^3 - 12x + 4$<br>
                                • $f''(x) = 12x^2 - 12$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Evaluate at $x_0 = 2.0$</div>
                                <p>• $f'(2) = 4(2)^3 - 12(2) + 4 = 32 - 24 + 4 = 12$<br>
                                • $f''(2) = 12(2)^2 - 12 = 48 - 12 = 36$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Apply Newton-Raphson Optimization Formula</div>
                                <p>$$x_1 = x_0 - \\frac{f'(x_0)}{f''(x_0)} = 2.0 - \\frac{12}{36} = 2.0 - \\frac{1}{3} = \\frac{5}{3} \\approx 1.6667$$</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (C) x_1 = 1.6667 (5/3)</div>
                        </div>
                    </details>
                </div>

                <!-- W4 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q8">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 8 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: Extremum Theorems, Convexity &amp; Search Methods</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding optimization principles and univariate numerical algorithms? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> By Weierstrass' Extreme Value Theorem, any continuous function $f(x)$ defined on a closed bounded interval $[a, b]$ is guaranteed to attain both a global minimum and a global maximum, which can occur at an interior stationary point ($f'(x) = 0$) OR at boundary endpoints ($x = a$ or $x = b$).</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> Maximizing $f(x)$ subject to $x \\in S$ is mathematically equivalent to minimizing $-f(x)$ over the same feasible set $S$, and $\\max f(x) = -\\min [-f(x)]$.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> The Golden Section search method reduces the uncertainty interval by a factor of $\\tau = \\frac{\\sqrt{5}-1}{2} \\approx 0.618$ per iteration without requiring any derivative evaluations.</li>
                            <li><span class="opt-bullet">[D]</span> If $f''(x^*) = 0$ at a stationary point $x^*$, the function $f(x)$ is guaranteed to have an inflection point at $x^*$.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> This is the Weierstrass theorem, essential for solving constrained boundary problems (e.g. Assignment 4 Q4).<br>
                                • <strong>[B] is TRUE:</strong> Min-max duality: flipping the sign of the objective function converts a maximization problem into an equivalent minimization problem.<br>
                                • <strong>[C] is TRUE:</strong> The Golden Section method uses the golden ratio $\\tau \\approx 0.61803$, re-evaluating only 1 new function point per iteration.<br>
                                • <strong>[D] is FALSE:</strong> If $f''(x^*) = 0$, the second-derivative test is inconclusive! For example, $f(x) = x^4$ has $f'(0) = 0$ and $f''(0) = 0$, but $x = 0$ is a strict global minimum, NOT an inflection point (because the first non-zero derivative is $f^{(4)}(0) = 24 &gt; 0$, an even order derivative).</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 5 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 5</span>
                        Multivariate Optimization, Hessians &amp; Constrained KKT Conditions
                    </h3>
                </div>

                <!-- W5 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q9">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 9 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: 2D Hessian Sylvester Criterion</span>
                    </div>
                    <div class="question-body">
                        <p>Consider the multivariable function $f(x_1, x_2) = x_1^3 + x_2^3 - 3x_1 x_2$. The point $(x_1, x_2) = (1, 1)$ is a stationary point because $\\nabla f(1, 1) = [0, 0]^T$. By computing the Hessian matrix $H(1, 1)$ and applying Sylvester's criterion, what is the nature of this stationary point?</p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">(A)</span> Local Minimum</li>
                            <li><span class="opt-bullet">(B)</span> Local Maximum</li>
                            <li><span class="opt-bullet">(C)</span> Saddle Point</li>
                            <li><span class="opt-bullet">(D)</span> Inconclusive Test</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Second Partial Derivatives</div>
                                <p>• $\\frac{\\partial f}{\\partial x_1} = 3x_1^2 - 3x_2 \\implies \\frac{\\partial^2 f}{\\partial x_1^2} = 6x_1$<br>
                                • $\\frac{\\partial f}{\\partial x_2} = 3x_2^2 - 3x_1 \\implies \\frac{\\partial^2 f}{\\partial x_2^2} = 6x_2$<br>
                                • $\\frac{\\partial^2 f}{\\partial x_1 \\partial x_2} = -3$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Construct Hessian at $(1, 1)$</div>
                                <p>$$H(1, 1) = \\begin{bmatrix} 6(1) & -3 \\\\ -3 & 6(1) \\end{bmatrix} = \\begin{bmatrix} 6 & -3 \\\\ -3 & 6 \\end{bmatrix}$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Apply Sylvester's Determinant Test</div>
                                <p>• First principal minor: $M_1 = 6 &gt; 0$<br>
                                • Second principal minor (determinant): $\\det(H) = (6)(6) - (-3)(-3) = 36 - 9 = 27 &gt; 0$<br>
                                Since $M_1 &gt; 0$ and $\\det(H) &gt; 0$, the Hessian is strictly <strong>positive definite</strong> ($H \\succ 0$). Therefore, $(1, 1)$ is a strict <strong>local minimum</strong>.</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (A) Local Minimum</div>
                        </div>
                    </details>
                </div>

                <!-- W5 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q10">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 10 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: KKT Conditions &amp; Steepest Descent Dynamics</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding constrained optimization, KKT conditions, and gradient descent? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> In the Method of Steepest Descent with an exact line search $\\min_{\\alpha &gt; 0} f(x_k + \\alpha d_k)$, any two consecutive search directions are mutually orthogonal: $d_{k+1}^T d_k = 0$.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> For a constrained problem $\\min f(x)$ subject to inequality constraints $g_j(x) \\le 0$, the KKT complementary slackness condition requires that $\\mu_j g_j(x^*) = 0$ for every constraint $j$.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> If an inequality constraint $g_1(x) \\le 0$ is strictly inactive at the optimum (i.e. $g_1(x^*) &lt; 0$), then its corresponding Lagrange multiplier must be identically zero ($\\mu_1 = 0$).</li>
                            <li><span class="opt-bullet">[D]</span> For a minimization problem with constraints $g_j(x) \\le 0$, the KKT dual feasibility condition requires that all multipliers $\\mu_j \\le 0$.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> In exact line search, $\\frac{d}{d\\alpha} f(x_k + \\alpha d_k) = \\nabla f(x_{k+1})^T d_k = 0$. Since $d_{k+1} = -\\nabla f(x_{k+1})$, we get $d_{k+1}^T d_k = 0$.<br>
                                • <strong>[B] is TRUE:</strong> The complementary slackness condition states that either $\\mu_j = 0$ or $g_j(x^*) = 0$, hence the product $\\mu_j g_j(x^*) = 0$ always holds.<br>
                                • <strong>[C] is TRUE:</strong> Follows directly from complementary slackness: if $g_1(x^*) &lt; 0$ (inactive), then to satisfy $\\mu_1 g_1(x^*) = 0$, $\\mu_1$ must be 0.<br>
                                • <strong>[D] is FALSE:</strong> In standard minimization with $g_j(x) \\le 0$, dual feasibility strictly requires $\\mu_j \\ge 0$ (non-negative), not non-positive!</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 6 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 6</span>
                        Linear Regression, ANOVA Partitioning &amp; Regression Diagnostics
                    </h3>
                </div>

                <!-- W6 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q11">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 11 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: ANOVA Table &amp; F-Statistic Computation</span>
                    </div>
                    <div class="question-body">
                        <p>A multiple linear regression model with $p = 3$ predictor variables is fitted to a dataset of $n = 24$ observations. The ANOVA decomposition yields:</p>
                        $$\\text{SST} = 500, \\quad \\text{SSE} = 100$$
                        <p>What are the values of the coefficient of determination $R^2$ and the overall model $F$-statistic?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> $R^2 = 0.20, \\quad F = 6.67$</li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> $R^2 = 0.80, \\quad F = 26.67$</li>
                            <li><span class="opt-bullet">(C)</span> $R^2 = 0.80, \\quad F = 80.00$</li>
                            <li><span class="opt-bullet">(D)</span> $R^2 = 0.75, \\quad F = 20.00$</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Compute Regression Sum of Squares (SSR)</div>
                                <p>By the ANOVA identity: $\\text{SST} = \\text{SSR} + \\text{SSE}$<br>
                                $$\\text{SSR} = \\text{SST} - \\text{SSE} = 500 - 100 = 400$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Calculate $R^2$</div>
                                <p>$$R^2 = \\frac{\\text{SSR}}{\\text{SST}} = \\frac{400}{500} = 0.80 \\quad (80\\%)$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Calculate Mean Squares &amp; $F$-Statistic</div>
                                <p>• Degrees of freedom: $df_R = p = 3$, and $df_E = n - p - 1 = 24 - 3 - 1 = 20$<br>
                                • $\\text{MSR} = \\frac{\\text{SSR}}{p} = \\frac{400}{3} = 133.333$<br>
                                • $\\text{MSE} = \\frac{\\text{SSE}}{n - p - 1} = \\frac{100}{20} = 5.00$<br>
                                • $F = \\frac{\\text{MSR}}{\\text{MSE}} = \\frac{133.333}{5.00} = 26.667 \\approx 26.67$</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) R^2 = 0.80, F = 26.67</div>
                        </div>
                    </details>
                </div>

                <!-- W6 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q12">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 12 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: Hat Matrix, Diagnostics &amp; Prediction Intervals</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding linear regression theory, matrices, and diagnostics? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> The Hat matrix $H = X(X^T X)^{-1} X^T$ is symmetric ($H = H^T$), idempotent ($H^2 = H$), and its trace equals the number of model parameters: $\\text{tr}(H) = p + 1$.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> In any ordinary least squares linear regression model that includes an intercept term $\\beta_0$, the sum and mean of the residuals are mathematically guaranteed to be identically zero: $\\sum_{i=1}^n e_i = 0$.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> At any fixed predictor value $X = x_0$, the Prediction Interval for an individual response $Y_0$ is strictly WIDER than the Confidence Interval for the mean response $E[Y \mid X = x_0]$ because the prediction interval must also account for the random error variance $\\sigma^2$ of the new observation.</li>
                            <li><span class="opt-bullet">[D]</span> Adding a new predictor variable to a linear regression model will always cause the Adjusted $R^2$ ($R_{adj}^2$) to increase, regardless of whether the variable is statistically significant.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> $H^T = (X(X^T X)^{-1} X^T)^T = H$, and $H^2 = X(X^T X)^{-1} X^T X (X^T X)^{-1} X^T = H$. Trace is $\\text{tr}(H) = \\text{tr}((X^T X)^{-1} X^T X) = \\text{tr}(I_{p+1}) = p + 1$.<br>
                                • <strong>[B] is TRUE:</strong> The normal equation for the intercept requires $\\frac{\\partial \\text{SSE}}{\\partial \\beta_0} = -2 \\sum (Y_i - \\hat{Y}_i) = 0 \\implies \\sum e_i = 0$.<br>
                                • <strong>[C] is TRUE:</strong> $\\text{Var}(\\hat{Y}_0 - Y_0) = \\sigma^2 \\left[1 + x_0^T (X^T X)^{-1} x_0\\right]$, which includes the additional $+1 \\sigma^2$ variance, making the interval strictly wider.<br>
                                • <strong>[D] is FALSE:</strong> While unadjusted $R^2$ never decreases, Adjusted $R^2 = 1 - \\frac{\\text{MSE}}{\\text{MST}}$ will DECREASE if the added predictor fails to decrease MSE enough to offset the loss of a degree of freedom!</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 7 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 7</span>
                        Logistic Regression, Odds Ratios &amp; Classification Performance
                    </h3>
                </div>

                <!-- W7 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q13">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 13 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: Logistic Regression Odds Ratio &amp; Probability</span>
                    </div>
                    <div class="question-body">
                        <p>A logistic regression model predicting cardiac disease ($Y = 1$) is fitted with age ($X_1$) as a predictor:</p>
                        $$\\ln\\left(\\frac{p}{1 - p}\\right) = -3.0 + 0.05 X_1$$
                        <p>What is the Odds Ratio (OR) associated with a 10-year increase in age, and what is the predicted probability of cardiac disease for an individual aged 60?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> $\\text{OR} = 1.05, \\quad p = 0.6000$</li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> $\\text{OR} = e^{0.5} \\approx 1.6487, \\quad p = 0.5000$</li>
                            <li><span class="opt-bullet">(C)</span> $\\text{OR} = 0.50, \\quad p = 0.2689$</li>
                            <li><span class="opt-bullet">(D)</span> $\\text{OR} = e^{0.05} \\approx 1.0513, \\quad p = 0.7311$</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Compute Odds Ratio for 10-Unit Increase</div>
                                <p>For a $\\Delta X = 10$ unit increase in $X_1$:<br>
                                $$\\text{OR} = e^{\\beta_1 \\Delta X} = e^{0.05 \\times 10} = e^{0.5} \\approx 1.6487$$<br>
                                This means the odds of heart disease increase by approximately 64.9% for every 10 years of age.</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Evaluate Logit at $X_1 = 60$</div>
                                <p>$$\\text{Logit} = -3.0 + 0.05(60) = -3.0 + 3.0 = 0$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 3: Convert Logit to Probability</div>
                                <p>$$p = \\frac{1}{1 + e^{-\\text{Logit}}} = \\frac{1}{1 + e^{-0}} = \\frac{1}{1 + 1} = \\frac{1}{2} = 0.5000$$</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) OR = e^{0.5} ≈ 1.6487, p = 0.5000</div>
                        </div>
                    </details>
                </div>

                <!-- W7 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q14">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 14 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: Cross-Validation &amp; Confusion Matrix Metrics</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding classification metrics, model validation, and logistic regression? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> The $F_1$-score is defined as the harmonic mean of Precision and Recall: $F_1 = \\frac{2 \\times \\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2\\text{TP}}{2\\text{TP} + \\text{FP} + \\text{FN}}$.</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> In Leave-One-Out Cross-Validation (LOOCV) for linear regression, the cross-validation error can be calculated from a single fit of the full model using diagonal elements $h_{ii}$ of the Hat matrix: $\\text{CV}_{(n)} = \\frac{1}{n} \\sum_{i=1}^n \\left(\\frac{e_i}{1 - h_{ii}}\\right)^2$.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> A Receiver Operating Characteristic (ROC) curve plots Sensitivity (True Positive Rate) on the Y-axis against (1 - Specificity) (False Positive Rate) on the X-axis across all classification thresholds $\\tau \\in [0, 1]$.</li>
                            <li><span class="opt-bullet">[D]</span> Bias-Variance tradeoff is classified as an empirical cross-validation technique along with $k$-fold cross-validation and validation set approach.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> Harmonic mean balances Precision and Recall, heavily penalizing models that sacrifice one for the other.<br>
                                • <strong>[B] is TRUE:</strong> This remarkable algebraic shortcut taught in Week 7 Lecture 39 avoids refitting the model $n$ times.<br>
                                • <strong>[C] is TRUE:</strong> This is the exact definition of an ROC curve. The area under this curve is the AUC.<br>
                                • <strong>[D] is FALSE:</strong> Lethal NPTEL Exam Trap! Bias-Variance tradeoff is a fundamental theoretical property of statistical learning models, NOT a cross-validation method (Assignment 7 Q1)!</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: [A], [B], and [C]</div>
                        </div>
                    </details>
                </div>

                <!-- ---------------------------------------------------- -->
                <!-- WEEK 8 EXAM QUESTIONS -->
                <!-- ---------------------------------------------------- -->
                <div style="margin: 28px 0 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
                    <h3 style="color: var(--primary-navy); margin: 0; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
                        <span style="background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">Week 8</span>
                        KNN, K-Means Clustering &amp; Unsupervised Learning
                    </h3>
                </div>

                <!-- W8 MCQ -->
                <div class="question-card filter-item filter-mcq" id="bank-q15">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-mcq">🎯 NPTEL MCQ (Single Correct)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 15 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #f1f5f9; color: #475569;">Topic: K-Means Conservation Law &amp; Standardized Data</span>
                    </div>
                    <div class="question-body">
                        <p>A data scientist applies $K$-Means clustering to a standardized dataset containing $n = 51$ observations and $p = 4$ continuous features (each feature has sample mean 0 and sample variance 1). After clustering with $K = 3$, the total within-cluster sum of squares is found to be $\\text{WSS} = 60.0$. What is the Between-Cluster Sum of Squares (BCSS) for this clustering?</p>
                        <ul class="options-list">
                            <li><span class="opt-bullet">(A)</span> $\\text{BCSS} = 144.0$</li>
                            <li class="correct-option"><span class="opt-bullet">(B)</span> $\\text{BCSS} = 140.0$</li>
                            <li><span class="opt-bullet">(C)</span> $\\text{BCSS} = 200.0$</li>
                            <li><span class="opt-bullet">(D)</span> Cannot be determined without cluster centroid coordinates</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Step 1: Compute Total Sum of Squares (TSS) for Standardized Data</div>
                                <p>For standardized data with $n$ samples and $p$ features, each feature contributes $(n-1)s_j^2 = (n-1)(1) = n-1$ to TSS:<br>
                                $$\\text{TSS} = (n - 1) \\times p = (51 - 1) \\times 4 = 50 \\times 4 = 200.0$$</p>
                            </div>
                            <div class="step-block">
                                <div class="step-title">Step 2: Apply K-Means Conservation Law</div>
                                <p>$$\\text{TSS} = \\text{BCSS} + \\text{WSS}$$
                                $$\\text{BCSS} = \\text{TSS} - \\text{WSS} = 200.0 - 60.0 = 140.0$$</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Answer: (B) BCSS = 140.0</div>
                        </div>
                    </details>
                </div>

                <!-- W8 MSQ -->
                <div class="question-card filter-item filter-msq" id="bank-q16">
                    <div class="question-header">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="q-tag q-tag-msq">☑️ NPTEL MSQ (Multi-Select)</span>
                            <span style="font-size: 0.76rem; font-weight: 700; color: #64748b;">Question 16 • [2 Marks]</span>
                        </div>
                        <span class="q-tag" style="background: #fdf2f8; color: #9d174d;">Topic: KNN Mechanics &amp; Clustering Properties</span>
                    </div>
                    <div class="question-body">
                        <p>Which of the following statements is/are <strong>TRUE</strong> regarding K-Nearest Neighbors (KNN) and K-Means clustering? <em>(Select all options that apply)</em></p>
                        <ul class="options-list">
                            <li class="correct-option"><span class="opt-bullet">[A]</span> In KNN, choosing $K = 1$ leads to a highly complex, flexible decision boundary with zero training error, which corresponds to low bias but high variance (overfitting).</li>
                            <li class="correct-option"><span class="opt-bullet">[B]</span> Standardizing/normalizing features prior to running KNN or K-Means is essential because distance metrics like Euclidean distance are sensitive to the arbitrary measurement units of the features.</li>
                            <li class="correct-option"><span class="opt-bullet">[C]</span> Lloyd's algorithm for K-Means clustering is sensitive to initial centroid placement and can converge to a local minimum; running the algorithm multiple times (e.g. <code class="inline-code">nstart = 20</code> in R) mitigates this problem.</li>
                            <li class="correct-option"><span class="opt-bullet">[D]</span> In K-Means clustering, as the number of clusters $K$ increases from 1 to $n$, the within-cluster sum of squares (WSS) monotonically decreases, reaching exactly 0 when $K = n$.</li>
                        </ul>
                    </div>
                    <details class="solution-drawer">
                        <summary><span>💡 View Step-by-Step Solution &amp; Distractor Analysis</span><span>▼</span></summary>
                        <div class="solution-content">
                            <div class="step-block">
                                <div class="step-title">Statement-by-Statement Evaluation</div>
                                <p>• <strong>[A] is TRUE:</strong> With $K=1$, each training point forms its own Voronoi cell, memorizing the training data perfectly.<br>
                                • <strong>[B] is TRUE:</strong> Features with larger numerical ranges (e.g. salary in thousands vs age in tens) dominate the distance metric unless standardized.<br>
                                • <strong>[C] is TRUE:</strong> Lloyd's heuristic guarantees convergence only to a local optimum. Setting <code class="inline-code">nstart = 20</code> evaluates 20 random starts and returns the one with lowest total WSS.<br>
                                • <strong>[D] is TRUE:</strong> When $K = n$, every point is its own cluster centroid, so distance from each point to its centroid is 0, making $\\text{WSS} = 0$.</p>
                            </div>
                            <div class="final-answer-box">✅ Correct Options: All four options [A], [B], [C], and [D] are TRUE!</div>
                        </div>
                    </details>
                </div>

            </div>
        </article>
    """
